# GitHub : réparer les contrôles CI

Diagnostiquer les contrôles GitHub Actions en échec d'une pull request, proposer une correction et vérifier son effet dans le périmètre autorisé.

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

Pour une CI de pull request défaillante sur GitHub Actions. Les autres fournisseurs de CI sont signalés par leur lien mais restent hors du périmètre de ce skill.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Copie locale du dépôt et branche courante ; numéro ou URL de PR si nécessaire.

### Exemple de demande

```text
Utilise $gh-fix-ci pour diagnostiquer les checks GitHub Actions
en échec de cette PR. Donne les logs utiles, propose le plan
de correction et précise les vérifications nécessaires.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Diagnostic CI | Nom du check, lien du run, extrait utile et contexte de l'échec. | Synthèse ; données JSON optionnelles via le script fourni. |
| Plan et correction | Solution proposée puis modifications lorsqu'elles sont autorisées. | Plan dans la conversation et fichiers du dépôt. |
| État de vérification | Tests effectués, checks consultés et échecs ou limites restants. | Bilan traçable ; aucune réussite supposée avant constat. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill gh-fix-ci
python scripts/install_local.py --skill gh-fix-ci --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

### Prérequis techniques

- GitHub CLI gh installé et authentifié pour le dépôt et les workflows concernés.
- Accès réseau autorisé et Python si le script d'inspection fourni est utilisé.

## Fonctionnement détaillé

1. Vérifier l'authentification gh et identifier la pull request.
2. Lire les checks et logs utiles, en contrôlant le commit auquel ils correspondent.
3. Résumer les échecs et proposer un plan de correction ; le skill amont prévoit une approbation avant implémentation.
4. Appliquer les corrections autorisées, exécuter les tests adaptés puis examiner les checks pertinents.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [scripts/](scripts) | Scripts fournis pour les opérations techniques décrites dans le skill. |
| [assets/](assets) | Icônes ou ressources utilisées par le skill. |

### Pour approfondir

- [Script d’inspection](scripts/inspect_pr_checks.py).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Ce guide français documente l'import OpenAI ; ses instructions et scripts amont restent inchangés. Le script d'inspection peut retourner un code non nul tant que des contrôles restent en échec. Les étapes d'approbation du skill doivent être interprétées avec les autorisations applicables à la session.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE). Les fichiers importés d’OpenAI conservent leur [licence Apache 2.0](LICENSE.txt) et leurs avis d’origine.
