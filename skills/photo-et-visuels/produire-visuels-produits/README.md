# Produire des visuels produits

Extraire, retoucher ou composer des visuels commerciaux qui restent fidèles au produit : contenu, emballages, quantités, étiquettes et proportions relatives.

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

Pour un packshot, un coffret, une extraction de catalogue, un fond blanc ou des déclinaisons destinées à une fiche e-commerce.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Référence et variante exactes, catalogue ou photographies sources suffisamment lisibles.
- Composition, quantités et dimensions connues ; photo étalon si les rapports de taille sont importants.
- Usage, canal, fond et formats d'export demandés.

### Exemple de demande

```text
Utilise $produire-visuels-produits pour ce coffret. Prépare un
visuel sur fond blanc en conservant les deux formats de terrines
et leurs proportions d'après les photographies jointes.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Fiche de contrôle | Sources, invariants, mesures disponibles et points restant à confirmer. | Tableau ou synthèse. |
| Visuel principal | Extraction fidèle ou édition contrôlée de la référence demandée. | Fichier image réellement créé, selon le format demandé et l'outil. |
| Déclinaisons | Versions nommées par référence et usage, accompagnées d'un aperçu. | Images exportées ; sources conservées quand disponibles. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill produire-visuels-produits
python scripts/install_local.py --skill produire-visuels-produits --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Identifier la référence et choisir entre extraction, édition et création de scène.
2. Fixer les invariants : produits inclus, échelle relative, marque, étiquettes et accessoires décoratifs.
3. Réaliser une version principale avec les outils adaptés et la comparer aux sources.
4. Après contrôle, décliner et vérifier recadrage, lisibilité, détourages et ombres.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Fiche produit visuelle](references/controle-produit.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Un poids ne permet pas de déduire les dimensions d'un bocal. Les textes ou certifications manquants ne sont pas inventés. La conformité visuelle à un canal ne vaut pas acceptation de l'image par la marketplace.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
