# Revue des pratiques de sécurité

## But

Examiner les pratiques de sécurité du code ou guider une implémentation plus sûre à partir des langages et frameworks réellement présents.

## Quand l'utiliser

Sur demande explicite de revue ou de conseils de sécurité, pour Python, JavaScript/TypeScript et Go. Le périmètre documenté ne couvre pas directement PHP ou C#.

## Informations à fournir

- Dépôt ou chemins concernés, langages, frameworks et contexte d'usage disponibles.
- Objectif : recommandations, rapport ou correction d'un problème identifié.
- Contraintes du projet et procédure de test/revue à respecter.

## Fonctionnement

1. Identifier la stack et consulter les références de sécurité applicables.
2. Examiner le code et relier les constats à des emplacements précis.
3. Prioriser les problèmes et expliquer leurs conséquences concrètes.
4. Pour un rapport, le rédiger puis présenter la synthèse ; traiter les corrections autorisées sans ignorer les risques de régression.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Recommandations | Pratiques adaptées au framework et au contexte réel. | Conseils ou changements ciblés selon la demande. |
| Rapport | Résumé, constats identifiés par gravité, impacts et références de code avec lignes. | security_best_practices_report.md, ou chemin demandé, lorsqu'un rapport est produit. |
| Corrections et contrôles | Modifications liées aux constats retenus et tests adaptés. | Fichiers du projet et bilan si la correction fait partie du périmètre autorisé. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $security-best-practices pour produire une revue
de sécurité de cette application Python. Relie chaque constat
au code et classe les corrections par gravité et impact.
```

## Limites et contrôles

Le rapport décrit les éléments examinés et ne certifie pas l'absence de vulnérabilités. Le skill amont prévoit une étape de lecture/accord avant la correction après rapport. Ce README français est local ; les références et instructions OpenAI sont conservées.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Références de sécurité](references).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence Apache 2.0 des fichiers importés](LICENSE.txt). Ce README français est une documentation locale sous [licence MIT](../../../LICENSE).
