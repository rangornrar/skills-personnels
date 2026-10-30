# Modéliser les menaces applicatives

Construire un modèle de menaces spécifique au dépôt et à son déploiement, fondé sur les actifs, entrées, flux et frontières de confiance observés.

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

Sur demande explicite de modélisation des menaces ou d'analyse des chemins d'abus d'un dépôt. Une simple présentation d'architecture ne nécessite pas ce workflow.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Dépôt ou sous-répertoire dans le périmètre, documentation et code accessibles.
- Usage, déploiement, exposition Internet, sensibilité des données et attentes d'authentification.
- Éléments hors périmètre et hypothèses connues, à préciser lorsqu'ils modifient les priorités.

### Exemple de demande

```text
Utilise $security-threat-model pour ce dépôt et son service
exposé sur Internet. Identifie les entrées et frontières de
confiance, puis prépare les questions de contexte avant le rapport.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Modèle du système | Composants, flux, frontières de confiance et preuves dans le dépôt. | Résumé et schéma Mermaid compact. |
| Analyse des menaces | Chemins d'abus, actifs touchés, priorités, mesures existantes et proposées. | Rapport Markdown avec hypothèses et questions ouvertes. |
| Fichier final | Rapport complet au format prévu par le skill. | <nom-du-depot-ou-dossier>-threat-model.md. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill security-threat-model
python scripts/install_local.py --skill security-threat-model --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Établir le système à partir de preuves du dépôt et séparer exécution, CI/outillage et exemples.
2. Identifier actifs, points d'entrée, frontières et capacités réalistes des attaquants.
3. Décrire les chemins d'abus et hiérarchiser impact et vraisemblance avec une justification qualitative.
4. Faire confirmer les hypothèses déterminantes puis proposer des mesures liées aux composants concernés.
5. Contrôler couverture, preuves et réserves avant de rédiger le rapport selon le contrat amont.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Contrat du rapport](references/prompt-template.md).
- [Actifs et contrôles](references/security-controls-and-assets.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Les scénarios de menace ne sont pas automatiquement des vulnérabilités confirmées. Les hypothèses non validées rendent certaines priorités conditionnelles. Le skill ne réalise pas un test d'intrusion ni un déploiement de correctifs. Le guide français est un ajout local à l'import OpenAI.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE). Les fichiers importés d’OpenAI conservent leur [licence Apache 2.0](LICENSE.txt) et leurs avis d’origine.
