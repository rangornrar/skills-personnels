# Préparer des fiches marketplaces

Préparer une fiche Amazon, Cdiscount ou autre marketplace à partir de données produit traçables, en séparant contenu éditorial, attributs et offre vendeur.

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

Pour rédiger un listing, compléter un fichier d'import, vérifier des données nutritionnelles ou examiner une erreur de catalogue.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Canal et pays, catégorie, référence, SKU et identifiants EAN/GTIN ou ASIN disponibles.
- Fiches fournisseur, étiquettes, composition, quantités, unités et données nutritionnelles sourcées.
- Modèle d'import ou champs à remplir ; pour une erreur, message complet et contexte.

### Exemple de demande

```text
Utilise $preparer-fiches-marketplaces pour préparer la fiche de
ce coffret. Rédige les contenus et une table des attributs sourcés ;
vérifie la base nutritionnelle avant de proposer les valeurs.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Textes prêts à copier | Titre, puces et description adaptés au produit et au canal. | Texte structuré. |
| Table d'attributs | Valeurs, sources, unités, bases de calcul et statuts à confirmer. | Tableau, Excel ou CSV selon la demande et les capacités disponibles. |
| Points bloquants | Données absentes, erreurs à traiter et vérifications avant import. | Liste de contrôle avec réserves. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill preparer-fiches-marketplaces
python scripts/install_local.py --skill preparer-fiches-marketplaces --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Rapprocher les sources, variantes et identifiants puis relever contradictions et lacunes.
2. Vérifier les règles actuelles du canal lorsqu'elles modifient les champs ou contenus attendus.
3. Rédiger titre, puces et description en conservant les caractéristiques établies.
4. Contrôler unités, base nutritionnelle et calculs, puis préparer les données dans le modèle demandé.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Données et calculs](references/donnees-et-calculs.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une moyenne calculée pour 100 g ne peut pas être copiée dans un champ par portion sans correspondance vérifiée. Le skill ne fabrique ni composition ni allégation. La préparation d'une fiche n'autorise pas sa publication.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
