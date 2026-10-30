# GitHub : traiter les commentaires

Transformer les commentaires de revue d'une pull request en corrections concrètes, en identifiant les points que l'utilisateur souhaite traiter.

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

Pour une PR ouverte correspondant à la branche courante, avec commentaires de revue ou d'issue à examiner. Ce skill n'est pas une revue générale de tout le dépôt.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Copie du dépôt, branche courante et pull request ouverte associée.

### Exemple de demande

```text
Utilise $gh-address-comments pour examiner les commentaires de
revue de la PR associée à cette branche. Résume les points et
les modifications nécessaires avant de traiter la sélection.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Inventaire de revue | Commentaires, fils et travail nécessaire pour chaque point. | Liste numérotée ; extraction par le script fourni. |
| Corrections | Changements correspondant aux points retenus. | Fichiers du dépôt. |
| Synthèse de traitement | Points traités, contrôles et éléments restant à discuter. | Bilan dans la conversation. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill gh-address-comments
python scripts/install_local.py --skill gh-address-comments --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

### Prérequis techniques

- GitHub CLI gh authentifié et accès au dépôt.
- Python pour le script fourni et périmètre des commentaires à traiter.

## Fonctionnement détaillé

1. Vérifier l'authentification et récupérer les commentaires et fils de revue.
2. Numéroter les points et résumer la correction nécessaire pour chacun.
3. Faire préciser les commentaires à traiter lorsque la sélection n'est pas déjà déterminée par la demande.
4. Appliquer les corrections choisies et restituer les changements et contrôles utiles.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [scripts/](scripts) | Scripts fournis pour les opérations techniques décrites dans le skill. |
| [assets/](assets) | Icônes ou ressources utilisées par le skill. |

### Pour approfondir

- [Script de récupération](scripts/fetch_comments.py).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Le guide français est ajouté localement aux fichiers OpenAI conservés. Modifier le code ne signifie pas qu'une réponse a été publiée, qu'un fil a été résolu ou que la PR a été fusionnée ; ces actions doivent être demandées et constatées séparément.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE). Les fichiers importés d’OpenAI conservent leur [licence Apache 2.0](LICENSE.txt) et leurs avis d’origine.
