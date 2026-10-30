# Produire des contenus éditoriaux

Préparer une chronique ou un contenu vidéo sourcé, depuis le choix de l'angle jusqu'aux éléments de publication réellement demandés.

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

Pour une série éditoriale, un épisode d'actualités, un script court ou un pack comprenant visuels, sous-titres et métadonnées.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Public, ligne éditoriale, sujet, période, territoire, durée et supports visés.
- Sources proposées, épisodes ou gabarits existants et ressources disponibles.
- Liste des livrables attendus et outils accessibles pour image, audio ou montage.

### Exemple de demande

```text
Utilise $produire-contenus-editoriaux pour préparer un épisode
de trois actualités vérifiées sur la période indiquée. Sépare
le texte prononcé, les visuels, les sources et les métadonnées.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Sources et contenu | Affirmations vérifiées, liens directs, script ou chronique et réserves. | Document éditorial sourcé. |
| Pack vidéo | Montage, voix, couverture et source éditable selon la demande. | Fichiers médias uniquement s'ils ont réellement été produits. |
| Sous-titres et métadonnées | Sous-titres alignés sur la voix, titre, description et mots-clés. | SRT/VTT et textes de publication selon les pièces demandées. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill produire-contenus-editoriaux
python scripts/install_local.py --skill produire-contenus-editoriaux --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Vérifier les sujets et distinguer dates de publication, événements, annonces et résultats.
2. Construire l'angle et conserver la correspondance entre affirmations, sources et réserves.
3. Écrire pour le support en séparant audio, visuel et texte à l'écran si nécessaire.
4. Produire les pièces demandées avec les outils disponibles et contrôler durée, lisibilité et synchronisation.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Contrat de livraison éditorial](references/pack-editorial.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une piste non établie ne devient pas une actualité pour remplir un format. Une illustration ne prouve pas un événement. Le script n'est pas annoncé comme une vidéo finalisée et le pack n'est pas publié automatiquement.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
