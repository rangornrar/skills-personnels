#!/usr/bin/env python3
"""Vérifier la bibliothèque sans appeler de service externe."""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import yaml

from install_local import load_catalog

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.venv', '__pycache__', 'output', 'outputs', 'tmp'}


def files_under(path):
    return [p for p in path.rglob('*') if p.is_file() and not set(p.relative_to(path).parts) & IGNORED]


def links_in(text):
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    body = '\n'.join(lines)
    return re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)', body) + re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', body, re.M)


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    try:
        catalog = load_catalog(root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'Catalogue : {exc}']
    entries = catalog['skills']
    listed = {e['path'] for e in entries}
    discovered = {p.parent.relative_to(root).as_posix() for p in (root / 'skills').rglob('SKILL.md')}
    if listed != discovered:
        errors.append(f'Catalogue/dossiers différents : {sorted(listed ^ discovered)}')
    for entry in entries:
        base = root / entry['path']
        manifest = base / 'SKILL.md'
        try:
            if entry.get('readme') != entry['path'] + '/README.md' or not (base / 'README.md').is_file():
                raise ValueError('README utilisateur absent ou chemin incohérent dans le catalogue')
            text = manifest.read_text(encoding='utf-8')
            match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
            if not match:
                raise ValueError('frontmatter YAML incomplet')
            data = yaml.safe_load(match.group(1))
            if not isinstance(data, dict) or data.get('name') != entry['name']:
                raise ValueError('nom du frontmatter différent du catalogue')
            description = data.get('description')
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                raise ValueError('description vide, invalide ou trop longue')
            if not text[match.end():].strip():
                raise ValueError('corps vide')
            if re.search(r'^\s*\[TODO:.*\]\s*$', text, re.M):
                raise ValueError('consigne de scaffold non remplie')
            if entry['genre'] not in catalog['genres']:
                raise ValueError('genre inconnu')
            metadata = yaml.safe_load((base / 'agents/openai.yaml').read_text(encoding='utf-8'))
            interface = metadata.get('interface', {})
            for key in ('display_name', 'short_description', 'default_prompt'):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    raise ValueError(f'interface.{key} absent ou vide')
            if entry['origin'] == 'creation':
                if not 25 <= len(interface['short_description']) <= 64:
                    raise ValueError('short_description doit avoir entre 25 et 64 caractères')
                if '$' + entry['name'] not in interface['default_prompt']:
                    raise ValueError('default_prompt doit citer le skill')
            policy = metadata.get('policy', {})
            if not isinstance(policy, dict):
                raise ValueError('policy doit être un objet')
            if 'allow_implicit_invocation' in policy and not isinstance(policy['allow_implicit_invocation'], bool):
                raise ValueError('allow_implicit_invocation doit être booléen')
            for key in ('icon_small', 'icon_large'):
                if key in interface:
                    icon = (base / interface[key]).resolve()
                    if not icon.is_relative_to(base) or not icon.is_file():
                        raise ValueError(f'icône absente ou hors du skill : {key}')
                    if icon.suffix == '.svg':
                        ET.parse(icon)
            if entry['origin'] == 'openai' and not (base / 'LICENSE.txt').is_file():
                raise ValueError('licence de l’import absente')
        except (OSError, UnicodeError, ValueError, TypeError, AttributeError, yaml.YAMLError, ET.ParseError) as exc:
            errors.append(f'{entry["name"]} : {exc}')

    try:
        lock = json.loads((root / 'sources.lock.json').read_text(encoding='utf-8'))
        imports = lock['imports']
        if len({e['name'] for e in imports}) != len(imports):
            errors.append('Sources : imports dupliqués')
        expected = {e['name']: e for e in entries if e['origin'] != 'creation'}
        if set(expected) != {e['name'] for e in imports}:
            errors.append('Sources : liste des imports différente du catalogue')
        for entry in imports:
            reference = expected.get(entry['name'])
            if not reference or reference['path'] != entry['path']:
                errors.append(f'Source incohérente : {entry["name"]}')
                continue
            base = root / reference['path']
            actual = {p.relative_to(base).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files_under(base)}
            if actual != entry['files_sha256']:
                errors.append(f'Import ou reprise modifié : {entry["name"]}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Sources : {exc}')

    imported_dirs = [root / e['path'] for e in entries if e['origin'] == 'openai']
    for path in files_under(root):
        try:
            if path.suffix in ('.yaml', '.yml'):
                yaml.safe_load(path.read_text(encoding='utf-8'))
            if path.suffix == '.md' and (path.name == 'README.md' or not any(path.is_relative_to(d) for d in imported_dirs)):
                for target in links_in(path.read_text(encoding='utf-8')):
                    parsed = urlsplit(target.strip('<>'))
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    resolved = (path.parent / unquote(parsed.path)).resolve()
                    if not resolved.is_relative_to(root) or not resolved.exists():
                        errors.append(f'{path.relative_to(root)} : lien local invalide : {target}')
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f'{path.relative_to(root)} : {exc}')
    return errors


def main():
    errors = validate()
    if errors:
        print('\n'.join('ERREUR : ' + e for e in errors))
        return 1
    count = len(load_catalog(ROOT)['skills'])
    print(f'Validation réussie : {count} skills, catalogue, ressources et imports vérifiés.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
