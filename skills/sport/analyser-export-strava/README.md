# Analyser un export Strava

## But

Décrire l'évolution d'activités sportives à partir d'un export Strava ou de fichiers d'activités, avec des comparaisons justes et des graphiques explicites.

## Quand l'utiliser

Pour un bilan de volume, régularité, allure ou dénivelé sur des périodes définies, ou pour éclairer un objectif sportif sans diagnostic médical.

## Informations à fournir

- Export Strava ou fichiers d'activités et périodes à comparer.
- Types d'activités retenus, objectif éventuel et contexte utile des parcours.
- Pour un programme demandé : niveau, expérience, disponibilité et sensations pertinentes.

## Fonctionnement

1. Inspecter unités, fuseau, couverture, doublons et champs manquants de l'export.
2. Séparer les sports et définir des fenêtres comparables, ainsi que durée totale ou en mouvement.
3. Calculer les agrégats correctement et examiner l'effet du terrain, des pauses et du dénivelé.
4. Produire les graphiques et distinguer observation, explication plausible et limite des données.
5. Si demandé, proposer un premier cycle ajustable et des critères de réévaluation.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Bilan | Volume, régularité, allures comparables, dénivelé et réserves de couverture. | Rapport structuré, PDF si demandé et réalisable. |
| Graphiques et calculs | Séries datées, unités et définitions des agrégats. | Images exportables et tables de calcul utiles. |
| Programme initial | Séances et critères d'ajustement adaptés au contexte. | Seulement si un programme est demandé ; aucune promesse de chrono. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $analyser-export-strava pour comparer les six derniers
mois et les vingt derniers jours. Sépare course et marche,
explique les calculs et produis des graphiques exportables.
```

## Limites et contrôles

Les valeurs absentes ne sont pas des zéros. L'âge seul ne définit pas les zones d'entraînement. Un export ne permet pas de diagnostiquer une fatigue ou une douleur. Les traces GPS et adresses sont évitées dans un rapport partagé si elles ne servent pas l'analyse.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence MIT](../../../LICENSE).
