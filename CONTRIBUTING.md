# Contribuer à la bibliothèque

## Choisir la bonne ressource

Une modification de méthode appartient au skill concerné. Une règle propre à SnapSlate, Transcript ou à un autre dépôt applicatif reste dans sa documentation de projet. Éviter les doublons et les skills qui capturent toute demande générale.

Pour un nouveau skill, créer `skills/<genre>/<nom>/SKILL.md` avec un nom unique, une description de déclenchement précise et des instructions utiles. Ajouter seulement les références réellement nécessaires. Les métadonnées d'interface se trouvent dans `agents/openai.yaml`.

Ajouter aussi un `README.md` pour les utilisateurs : but, cas d'usage, informations à fournir, fonctionnement, livrables avec formats et conditions, exemple, limites et liens utiles. Distinguer les formats facultatifs des outputs systématiques. Le guide décrit le workflow ; les instructions de référence restent dans `SKILL.md`.

Organiser le README autour du lecteur : d'abord l'utilité, l'utilisation avec exemple et les sorties ; ensuite l'installation, le fonctionnement détaillé, l'architecture et les détails techniques. Ajouter un sommaire avec des liens vers les sections. Le README d'entrée de la bibliothèque suit la même logique.

## Tenir le catalogue

Mettre à jour `catalogue.json`, `CATALOGUE.md`, les exemples et le changelog pour tout ajout ou déplacement. Un dossier de genre ne constitue pas un skill et ne contient pas de `SKILL.md`.

Les créations sont en français et UTF-8. Les exemples sont fictifs ou anonymisés ; ne pas ajouter CV, enregistrements, traces GPS, données commerciales réelles ou secrets. Les fichiers de sortie vont hors du dépôt ou dans les répertoires ignorés.

## Modifier une reprise ou un import

Les trois reprises personnelles sont identifiées dans `sources.lock.json`. Une évolution est possible mais doit être décrite et les empreintes mises à jour explicitement après revue.

Pour les imports OpenAI, préférer une mise à jour depuis une révision amont. Conserver licences, assets et scripts. Si une adaptation locale devient nécessaire, la déclarer dans le catalogue et les attributions au lieu de présenter l'import comme inchangé.

Les README français sont des ajouts locaux identifiés dans `sources.lock.json` par `local_additions`. Après modification d'un de ces guides, actualiser son empreinte uniquement ; conserver celles des fichiers amont inchangés.

Lorsqu'un README déjà présent dans une reprise est adapté, déclarer la modification dans `local_modifications` avec son empreinte d'origine. Ne pas présenter cette adaptation comme une copie inchangée.

## Vérifier

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_library.py
python -m unittest discover -s tests -v
```

Pour un changement de comportement, exécuter aussi les scénarios pertinents décrits dans [la recette](docs/VALIDATION.md). Une PR indique le problème, le résultat, les contrôles réalisés et les limites. Ne pas déclarer un livrable PDF, un envoi ou une publication vérifié si cette étape n'a pas été exécutée.
