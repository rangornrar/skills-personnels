#!/usr/bin/env python3
"""Installer une sélection locale sans téléchargement ni écrasement."""

import argparse
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def load_catalog(root):
    root = Path(root).resolve()
    data = json.loads((root / 'catalogue.json').read_text(encoding='utf-8'))
    entries = data.get('skills')
    if not isinstance(entries, list) or not entries:
        raise ValueError('Catalogue vide ou invalide.')
    names = set()
    for entry in entries:
        name = entry.get('name', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in names:
            raise ValueError(f'Nom de skill invalide ou dupliqué : {name}')
        names.add(name)
        raw_path = Path(entry.get('path', ''))
        source = root / raw_path
        if raw_path.is_absolute() or len(raw_path.parts) != 3 or raw_path.parts[0] != 'skills':
            raise ValueError(f'Chemin de skill invalide : {raw_path}')
        if source.name != name or raw_path.parts[1] != entry.get('genre'):
            raise ValueError(f'Chemin incohérent pour {name}.')
        if not source.resolve().is_relative_to(root / 'skills') or not (source / 'SKILL.md').is_file():
            raise ValueError(f'Source absente ou hors bibliothèque : {name}')
        if any(part.is_symlink() for part in [source, *source.parents] if part.is_relative_to(root)):
            raise ValueError(f'Lien symbolique interdit dans la source : {name}')
    return data


def select_entries(catalog, names=(), genres=(), select_all=False):
    entries = catalog['skills']
    names, genres = set(names), set(genres)
    unknown_names = names - {e['name'] for e in entries}
    unknown_genres = genres - set(catalog['genres'])
    if unknown_names or unknown_genres:
        raise ValueError(f'Sélection inconnue : {sorted(unknown_names | unknown_genres)}')
    if not (select_all or names or genres):
        raise ValueError('Choisir --skill, --genre ou --all ; utiliser --list pour parcourir.')
    return [e for e in entries if select_all or e['name'] in names or e['genre'] in genres]


def install(root, entries, destination, apply=False):
    root, destination = Path(root).resolve(), Path(destination).expanduser().resolve()
    plan = []
    # Préparer toutes les copies avant la première écriture.
    for entry in entries:
        source = (root / entry['path']).resolve()
        target = destination / entry['name']
        if not source.is_relative_to(root / 'skills') or target.parent != destination:
            raise ValueError('Chemin hors du périmètre prévu.')
        if destination == source or destination.is_relative_to(source):
            raise ValueError('La destination ne peut pas être dans le skill source.')
        if target.exists() or target.is_symlink():
            raise FileExistsError(f'Installation existante, aucune copie effectuée : {target}')
        if any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError(f'Lien symbolique dans le skill {entry["name"]}.')
        plan.append((source, target))
    if apply:
        destination.mkdir(parents=True, exist_ok=True)
        for source, target in plan:
            # Pas d'écrasement ; en cas d'erreur disque, signaler l'échec sans supprimer les copies.
            shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='Lister le catalogue sans installer.')
    parser.add_argument('--skill', action='append', default=[], help='Nom à installer ; répétable.')
    parser.add_argument('--genre', action='append', default=[], help='Genre à installer ; répétable.')
    parser.add_argument('--all', action='store_true', help='Sélectionner tous les skills.')
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents' / 'skills')
    parser.add_argument('--apply', action='store_true', help='Effectuer les copies prévues.')
    args = parser.parse_args()
    try:
        catalog = load_catalog(ROOT)
        if args.list:
            for entry in catalog['skills']:
                print(f'{entry["genre"]:30} {entry["name"]:40} {entry["origin"]}')
            return 0
        entries = select_entries(catalog, args.skill, args.genre, args.all)
        for source, target in install(ROOT, entries, args.dest, args.apply):
            print(f'{"COPIÉ" if args.apply else "PRÉVU"} : {source.name} -> {target}')
        if not args.apply:
            print('Simulation : ajouter --apply pour effectuer les copies.')
        else:
            print('Copies terminées. Si nécessaire, redémarrer le client pour découvrir les skills.')
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERREUR : {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
