# Revue des pratiques de sécurité

Examiner les pratiques de sécurité du code ou guider une implémentation plus sûre à partir des langages et frameworks réellement présents.

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

Sur demande explicite de revue ou de conseils de sécurité, pour Python, JavaScript/TypeScript et Go. Le périmètre documenté ne couvre pas directement PHP ou C#.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Dépôt ou chemins concernés, langages, frameworks et contexte d'usage disponibles.
- Objectif : recommandations, rapport ou correction d'un problème identifié.
- Contraintes du projet et procédure de test/revue à respecter.

### Exemple de demande

```text
Utilise $security-best-practices pour produire une revue
de sécurité de cette application Python. Relie chaque constat
au code et classe les corrections par gravité et impact.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Recommandations | Pratiques adaptées au framework et au contexte réel. | Conseils ou changements ciblés selon la demande. |
| Rapport | Résumé, constats identifiés par gravité, impacts et références de code avec lignes. | security_best_practices_report.md, ou chemin demandé, lorsqu'un rapport est produit. |
| Corrections et contrôles | Modifications liées aux constats retenus et tests adaptés. | Fichiers du projet et bilan si la correction fait partie du périmètre autorisé. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill security-best-practices
python scripts/install_local.py --skill security-best-practices --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Identifier la stack et consulter les références de sécurité applicables.
2. Examiner le code et relier les constats à des emplacements précis.
3. Prioriser les problèmes et expliquer leurs conséquences concrètes.
4. Pour un rapport, le rédiger puis présenter la synthèse ; traiter les corrections autorisées sans ignorer les risques de régression.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Références de sécurité](references).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Le rapport décrit les éléments examinés et ne certifie pas l'absence de vulnérabilités. Le skill amont prévoit une étape de lecture/accord avant la correction après rapport. Ce README français est local ; les références et instructions OpenAI sont conservées.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE). Les fichiers importés d’OpenAI conservent leur [licence Apache 2.0](LICENSE.txt) et leurs avis d’origine.
