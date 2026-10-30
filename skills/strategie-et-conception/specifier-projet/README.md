# Spécifier un projet

Transformer une idée de petit logiciel en spécifications fonctionnelles et techniques par entretien progressif, audit contradictoire et consolidation du dossier.

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

Pour cadrer une V1, challenger un cahier des charges, reprendre des décisions ou produire un dossier de travail avant développement.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Problème à résoudre, utilisateurs et exemple d'utilisation de bout en bout.
- Documents existants et versions ; objectifs, contraintes et décisions déjà prises.
- Pour une reprise : dernier dossier, source éditable et registre des questions ouvertes.

### Exemple de demande

```text
Utilise $specifier-projet pour cadrer un outil de suivi de matériel.
Il doit fonctionner hors connexion sous Windows. Commence par les
questions qui changent le périmètre et attends mes réponses.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Spécifications et arbitrages | Objectifs, V1, exigences, options techniques, décisions, risques et questions ouvertes. | État de travail actualisé. |
| Audit contradictoire | Constats reliés aux exigences, conséquences, gravité justifiée et corrections proposées. | Synthèse intégrée au dossier. |
| Dossier de spécifications | Couverture, version, statut, sommaire, spécifications, audit et recette. | PDF lorsque les capacités de génération et de rendu sont disponibles. |
| Source et reprise | Version éditable et informations permettant de continuer sans redemander les décisions closes. | Fichiers persistants ; format adapté aux outils, DOCX si demandé et réalisable. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill specifier-projet
python scripts/install_local.py --skill specifier-projet --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Lire le contexte, établir le périmètre et poser une à trois questions prioritaires à la fois.
2. Structurer les exigences et critères de recette avec des identifiants stables.
3. Auditer une même version sous huit regards, dédupliquer les constats et transformer les lacunes en questions utiles.
4. Intégrer les réponses et les arbitrages, réexaminer les impacts puis consolider lorsque la V1 est suffisamment claire.
5. Produire le dossier PDF aux jalons utiles ou sur demande, puis inspecter le rendu et conserver l'état de reprise.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |
| [assets/](assets) | Icônes ou ressources utilisées par le skill. |

### Pour approfondir

- [Domaines de questions](references/domaines.md).
- [Plan du dossier](references/plan-dossier.md).
- [Guide détaillé](../../../docs/specifier-projet/UTILISATION.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Les huit regards sont des perspectives de l'IA, pas des experts indépendants consultés. Une proposition reste proposée tant qu'elle n'est pas acceptée. Un dossier provisoire peut être livré avec ses réserves ; un faux PDF ne doit jamais être annoncé.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
