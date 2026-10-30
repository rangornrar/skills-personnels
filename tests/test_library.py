from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install_local import install, load_catalog, select_entries
from validate_library import validate


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.destination = Path(self.temp.name) / 'installed'
        self.catalog = load_catalog(ROOT)

    def tearDown(self):
        self.temp.cleanup()

    def test_selection_union_without_duplicates(self):
        entries = select_entries(self.catalog, names=['preparer-fiches-marketplaces'], genres=['commerce'])
        self.assertEqual({e['name'] for e in entries}, {'preparer-fiches-marketplaces', 'piloter-ca-et-marges'})

    def test_unknown_selection_rejected(self):
        with self.assertRaises(ValueError):
            select_entries(self.catalog, names=['unknown'])

    def test_no_selection_rejected(self):
        with self.assertRaises(ValueError):
            select_entries(self.catalog)

    def test_dry_run_has_no_writes(self):
        entries = select_entries(self.catalog, genres=['commerce'])
        self.assertEqual(len(install(ROOT, entries, self.destination)), 2)
        self.assertFalse(self.destination.exists())

    def test_resources_copied(self):
        entries = select_entries(self.catalog, names=['preparer-seance-photo'])
        install(ROOT, entries, self.destination, apply=True)
        target = self.destination / 'preparer-seance-photo'
        for source in (ROOT / entries[0]['path']).rglob('*'):
            if source.is_file():
                self.assertEqual(source.read_bytes(), (target / source.relative_to(ROOT / entries[0]['path'])).read_bytes())

    def test_all_collisions_checked_before_first_write(self):
        entries = select_entries(self.catalog, genres=['commerce'])
        existing = self.destination / entries[-1]['name']
        existing.mkdir(parents=True)
        marker = existing / 'custom.txt'
        marker.write_text('keep', encoding='utf-8')
        with self.assertRaises(FileExistsError):
            install(ROOT, entries, self.destination, apply=True)
        self.assertFalse((self.destination / entries[0]['name']).exists())
        self.assertEqual(marker.read_text(encoding='utf-8'), 'keep')


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'library'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__', '.git'))

    def tearDown(self):
        self.temp.cleanup()

    def test_library_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_modified_import_detected(self):
        path = self.root / 'skills/developpement/gh-fix-ci/LICENSE.txt'
        path.write_bytes(path.read_bytes() + b'\nchanged\n')
        self.assertTrue(any('gh-fix-ci' in e and 'modifi' in e for e in validate(self.root)))

    def test_missing_local_target_detected(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n[missing](absent.md)\n')
        self.assertTrue(any('lien local invalide' in e for e in validate(self.root)))

    def test_invalid_yaml_detected(self):
        (self.root / 'skills/commerce/piloter-ca-et-marges/agents/openai.yaml').write_text('interface: [', encoding='utf-8')
        self.assertTrue(validate(self.root))

    def test_catalog_escape_rejected(self):
        path = self.root / 'catalogue.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['skills'][0]['path'] = '../outside'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(validate(self.root))

    def test_unlisted_skill_detected(self):
        path = self.root / 'skills/commerce/unlisted/SKILL.md'
        path.parent.mkdir()
        path.write_text('---\nname: unlisted\ndescription: extra\n---\nBody\n', encoding='utf-8')
        self.assertTrue(any('Catalogue/dossiers' in e for e in validate(self.root)))


if __name__ == '__main__':
    unittest.main()
