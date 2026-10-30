# GitHub : traiter les commentaires

## But

Transformer les commentaires de revue d'une pull request en corrections concrètes, en identifiant les points que l'utilisateur souhaite traiter.

## Quand l'utiliser

Pour une PR ouverte correspondant à la branche courante, avec commentaires de revue ou d'issue à examiner. Ce skill n'est pas une revue générale de tout le dépôt.

## Informations à fournir

- Copie du dépôt, branche courante et pull request ouverte associée.
- GitHub CLI gh authentifié et accès au dépôt.
- Python pour le script fourni et périmètre des commentaires à traiter.

## Fonctionnement

1. Vérifier l'authentification et récupérer les commentaires et fils de revue.
2. Numéroter les points et résumer la correction nécessaire pour chacun.
3. Faire préciser les commentaires à traiter lorsque la sélection n'est pas déjà déterminée par la demande.
4. Appliquer les corrections choisies et restituer les changements et contrôles utiles.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Inventaire de revue | Commentaires, fils et travail nécessaire pour chaque point. | Liste numérotée ; extraction par le script fourni. |
| Corrections | Changements correspondant aux points retenus. | Fichiers du dépôt. |
| Synthèse de traitement | Points traités, contrôles et éléments restant à discuter. | Bilan dans la conversation. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $gh-address-comments pour examiner les commentaires de
revue de la PR associée à cette branche. Résume les points et
les modifications nécessaires avant de traiter la sélection.
```

## Limites et contrôles

Le guide français est ajouté localement aux fichiers OpenAI conservés. Modifier le code ne signifie pas qu'une réponse a été publiée, qu'un fil a été résolu ou que la PR a été fusionnée ; ces actions doivent être demandées et constatées séparément.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Script de récupération](scripts/fetch_comments.py).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence Apache 2.0 des fichiers importés](LICENSE.txt). Ce README français est une documentation locale sous [licence MIT](../../../LICENSE).
