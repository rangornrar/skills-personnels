# Analyser un export Strava

Décrire l'évolution d'activités sportives à partir d'un export Strava ou de fichiers d'activités, avec des comparaisons justes et des graphiques explicites.

## Sommaire

- [À quoi cela sert](#à-quoi-cela-sert)
- [Comment l'utiliser](#comment-lutiliser)
- [Sorties attendues](#sorties-attendues)
- [Installation](#installation)
- [Fonctionnement détaillé](#fonctionnement-détaillé)
- [Architecture et ressources](#architecture-et-ressources)
- [Limites et contrôles](#limites-et-contrôles)
- [Licence](#licence)

## À quoi cela sert

Pour un bilan de volume, régularité, allure ou dénivelé sur des périodes définies, ou pour éclairer un objectif sportif sans diagnostic médical.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Export Strava ou fichiers d'activités et périodes à comparer.
- Types d'activités retenus, objectif éventuel et contexte utile des parcours.
- Pour un programme demandé : niveau, expérience, disponibilité et sensations pertinentes.

### Exemple de demande

```text
Utilise $analyser-export-strava pour comparer les six derniers
mois et les vingt derniers jours. Sépare course et marche,
explique les calculs et produis des graphiques exportables.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Bilan | Volume, régularité, allures comparables, dénivelé et réserves de couverture. | Rapport structuré, PDF si demandé et réalisable. |
| Graphiques et calculs | Séries datées, unités et définitions des agrégats. | Images exportables et tables de calcul utiles. |
| Programme initial | Séances et critères d'ajustement adaptés au contexte. | Seulement si un programme est demandé ; aucune promesse de chrono. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill analyser-export-strava
python scripts/install_local.py --skill analyser-export-strava --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Inspecter unités, fuseau, couverture, doublons et champs manquants de l'export.
2. Séparer les sports et définir des fenêtres comparables, ainsi que durée totale ou en mouvement.
3. Calculer les agrégats correctement et examiner l'effet du terrain, des pauses et du dénivelé.
4. Produire les graphiques et distinguer observation, explication plausible et limite des données.
5. Si demandé, proposer un premier cycle ajustable et des critères de réévaluation.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |

### Pour approfondir

- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Les valeurs absentes ne sont pas des zéros. L'âge seul ne définit pas les zones d'entraînement. Un export ne permet pas de diagnostiquer une fatigue ou une douleur. Les traces GPS et adresses sont évitées dans un rapport partagé si elles ne servent pas l'analyse.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
