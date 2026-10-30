# Contribuer à la bibliothèque

## Choisir la bonne ressource

Une modification de méthode appartient au skill concerné. Une règle propre à SnapSlate, Transcript ou à un autre dépôt applicatif reste dans sa documentation de projet. Éviter les doublons et les skills qui capturent toute demande générale.

Pour un nouveau skill, créer `skills/<genre>/<nom>/SKILL.md` avec un nom unique, une description de déclenchement précise et des instructions utiles. Ajouter seulement les références réellement nécessaires. Les métadonnées d'interface se trouvent dans `agents/openai.yaml`.

## Tenir le catalogue

Mettre à jour `catalogue.json`, `CATALOGUE.md`, les exemples et le changelog pour tout ajout ou déplacement. Un dossier de genre ne constitue pas un skill et ne contient pas de `SKILL.md`.

Les créations sont en français et UTF-8. Les exemples sont fictifs ou anonymisés ; ne pas ajouter CV, enregistrements, traces GPS, données commerciales réelles ou secrets. Les fichiers de sortie vont hors du dépôt ou dans les répertoires ignorés.

## Modifier une reprise ou un import

Les trois reprises personnelles sont identifiées dans `sources.lock.json`. Une évolution est possible mais doit être décrite et les empreintes mises à jour explicitement après revue.

Pour les imports OpenAI, préférer une mise à jour depuis une révision amont. Conserver licences, assets et scripts. Si une adaptation locale devient nécessaire, la déclarer dans le catalogue et les attributions au lieu de présenter l'import comme inchangé.

## Vérifier

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_library.py
python -m unittest discover -s tests -v
```

Pour un changement de comportement, exécuter aussi les scénarios pertinents décrits dans [la recette](docs/VALIDATION.md). Une PR indique le problème, le résultat, les contrôles réalisés et les limites. Ne pas déclarer un livrable PDF, un envoi ou une publication vérifié si cette étape n'a pas été exécutée.
