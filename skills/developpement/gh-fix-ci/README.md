# GitHub : réparer les contrôles CI

## But

Diagnostiquer les contrôles GitHub Actions en échec d'une pull request, proposer une correction et vérifier son effet dans le périmètre autorisé.

## Quand l'utiliser

Pour une CI de pull request défaillante sur GitHub Actions. Les autres fournisseurs de CI sont signalés par leur lien mais restent hors du périmètre de ce skill.

## Informations à fournir

- Copie locale du dépôt et branche courante ; numéro ou URL de PR si nécessaire.
- GitHub CLI gh installé et authentifié pour le dépôt et les workflows concernés.
- Accès réseau autorisé et Python si le script d'inspection fourni est utilisé.

## Fonctionnement

1. Vérifier l'authentification gh et identifier la pull request.
2. Lire les checks et logs utiles, en contrôlant le commit auquel ils correspondent.
3. Résumer les échecs et proposer un plan de correction ; le skill amont prévoit une approbation avant implémentation.
4. Appliquer les corrections autorisées, exécuter les tests adaptés puis examiner les checks pertinents.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Diagnostic CI | Nom du check, lien du run, extrait utile et contexte de l'échec. | Synthèse ; données JSON optionnelles via le script fourni. |
| Plan et correction | Solution proposée puis modifications lorsqu'elles sont autorisées. | Plan dans la conversation et fichiers du dépôt. |
| État de vérification | Tests effectués, checks consultés et échecs ou limites restants. | Bilan traçable ; aucune réussite supposée avant constat. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $gh-fix-ci pour diagnostiquer les checks GitHub Actions
en échec de cette PR. Donne les logs utiles, propose le plan
de correction et précise les vérifications nécessaires.
```

## Limites et contrôles

Ce guide français documente l'import OpenAI ; ses instructions et scripts amont restent inchangés. Le script d'inspection peut retourner un code non nul tant que des contrôles restent en échec. Les étapes d'approbation du skill doivent être interprétées avec les autorisations applicables à la session.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Script d’inspection](scripts/inspect_pr_checks.py).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence Apache 2.0 des fichiers importés](LICENSE.txt). Ce README français est une documentation locale sous [licence MIT](../../../LICENSE).
