# Préparer une séance photo

Passer d'une intention artistique à une séance réalisable : familles de poses, éclairages, continuité des tenues, accessoires et déroulé de prise de vue.

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

Pour préparer un shooting, un moodboard de poses ou un livret utilisable pendant la séance. Un packshot commercial isolé relève du skill de visuels produits.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Thème, références visuelles, usages des images, personne ou personnage et cadrages souhaités.
- Lieu, fond, matériel réellement disponible, tenues, accessoires et contraintes de séance.
- Si un atelier de moodboard existe : profils, formats et sorties disponibles.

### Exemple de demande

```text
Utilise $preparer-seance-photo pour une séance de portraits
sur fond gris avec une tenue et deux éclairages. Regroupe les poses
par famille et prépare un livret illustré pour la prise de vue.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Brief et déroulé | Intention, ordre des séquences, changements de tenue ou lumière et matériel. | Texte ou document de préparation. |
| Planche de poses | Poses regroupées par catégorie avec consignes et variantes distinctes. | Tableau et références visuelles disponibles. |
| Livret de séance | Photos ou illustrations, légendes et schémas d'éclairage utiles. | PDF rendu et inspecté si les outils le permettent ; source éditable lorsque possible. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill preparer-seance-photo
python scripts/install_local.py --skill preparer-seance-photo --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Établir le brief et confirmer les contraintes qui influencent la préparation.
2. Organiser les poses par familles et décrire appuis, mains, regard et cadrage.
3. Définir les lumières réalisables et les variations concrètes de tenue en conservant les invariants utiles.
4. Contrôler un échantillon des références produites avant une grande série, puis organiser le déroulé et le livret.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Fiche de préparation](references/preparation.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Les puissances et expositions proposées restent à calibrer sur place. Le prompt ne prouve pas que le moteur d'image respecte une tenue ou une identité. Le skill n'installe pas automatiquement ComfyUI ni un modèle local.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
