# Transcrire une réunion et ses actions

Passer d'un enregistrement ou d'une transcription à un compte rendu fidèle, en distinguant propos, propositions, décisions, actions et incertitudes.

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

Pour une réunion ou un entretien professionnel, avec transcription intégrale, synthèse ou suivi d'actions selon le besoin.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Enregistrements dans leur ordre ou transcription existante ; langue et participants connus.
- Date et objet de réunion lorsqu'ils sont établis ; type de restitution souhaité.
- Outils de transcription accessibles et autorisation adaptée si un service externe doit recevoir l'audio.

### Exemple de demande

```text
Utilise $transcrire-reunion-et-actions pour cette transcription.
Prépare un compte rendu de deux pages et un tableau d'actions ;
conserve les chiffres incertains dans les points à vérifier.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Transcription | Verbatim ou version nettoyée selon la demande, intervenants et incertitudes. | Texte avec horodatages si disponibles ; uniquement si l'audio est traité. |
| Compte rendu | Synthèse par sujet, décisions, désaccords et questions ouvertes. | Texte, DOCX ou PDF si demandé et réalisable. |
| Registre d'actions | Action, responsable, échéance et source ; données absentes à confirmer. | Tableau séparé ou intégré au compte rendu. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill transcrire-reunion-et-actions
python scripts/install_local.py --skill transcrire-reunion-et-actions --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Identifier les sources et exploiter les transcriptions disponibles avant de relancer un traitement.
2. Transcrire si nécessaire, conserver les repères temporels et marquer les passages incertains.
3. Contrôler les noms, chiffres et engagements déterminants à l'écoute lorsque possible.
4. Regrouper les sujets et extraire uniquement les décisions et actions étayées par les sources.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Structure de restitution](references/restitution.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une ambition évoquée n'est pas une décision validée. Un locuteur inconnu reste non identifié. Si seule une transcription est fournie, le skill ne prétend pas avoir vérifié l'audio. La rédaction ne vaut pas envoi aux participants.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
