# Rédiger des messages professionnels

Rédiger une réponse professionnelle naturelle, courte et directement utilisable, en conservant l'intention et les faits fournis.

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

Pour des emails, messages partenaires, réponses clients, relances, réclamations ou reformulations. Le compte rendu de réunion relève d'un autre workflow.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Message reçu ou brouillon à retravailler, ainsi que les faits à conserver.
- Auteur, destinataire, relation, objectif et action attendue.
- Ton, langue, tutoiement/vouvoiement et contrainte de longueur, s'ils sont précisés.

### Exemple de demande

```text
Utilise $rediger-messages-professionnels pour raccourcir cette
réponse client. Garde un ton courtois et simple, sans ajouter
d'engagement ni modifier les montants.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Message final | Une version prête à copier, fidèle aux faits et au ton demandé. | Texte ; objet inclus pour un email lorsque pertinent. |
| Points à compléter | Uniquement les ambiguïtés qui empêchent une formulation exacte. | Note courte ou question ciblée si nécessaire. |
| Variantes | Versions adaptées à un vrai choix de ton ou de longueur. | Seulement si demandées ou utiles à un arbitrage. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill rediger-messages-professionnels
python scripts/install_local.py --skill rediger-messages-professionnels --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Identifier qui parle à qui et l'objectif concret du message.
2. Retenir le contexte indispensable, formuler la réponse ou demande, puis la prochaine étape.
3. Supprimer les répétitions et adapter les formules au support et à la relation.
4. Relire identités, références, montants, dates et engagements avant de livrer.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |

### Pour approfondir

- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Le skill n'ajoute pas de promesse, geste commercial, disponibilité ou accord d'un tiers. Un numéro ambigu n'est pas corrigé silencieusement. Il prépare un message sans l'envoyer automatiquement.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
