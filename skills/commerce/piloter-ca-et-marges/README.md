# Piloter le CA et les marges

Construire un suivi du réalisé, un atterrissage commercial et une analyse des marges par canal ou référence, avec des hypothèses explicites et des calculs actualisables.

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

Pour rapprocher factures, commandes, prospection et exports marketplaces, comparer des périodes ou examiner la rentabilité d'un scénario.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Période, date d'arrêté, canaux, devise et définition du CA retenue.
- Factures, avoirs, commandes, données de prospection et historiques utiles.
- Prix, volumes, coûts et frais avec unités, assiettes et périodicités ; hypothèses connues.

### Exemple de demande

```text
Utilise $piloter-ca-et-marges pour rapprocher ces factures et
commandes puis préparer l'atterrissage de fin d'année par canal.
Sépare les hypothèses de volume et les frais de calcul de marge.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Modèle commercial | Sources, rapprochements, hypothèses et synthèse par canal. | Classeur Excel ou autre tableur disponible, si demandé. |
| Atterrissage | Réalisé, ferme, prévision complémentaire et comparatif à périmètre constant. | Tableau de synthèse et scénarios conditionnels. |
| Analyse de marge | Coûts inclus, assiettes, marge de contribution et réserves. | Calculs traçables ; graphiques si utiles. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill piloter-ca-et-marges
python scripts/install_local.py --skill piloter-ca-et-marges --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Rapprocher les ventes par clés, séparer leurs états et repérer doublons ou données manquantes.
2. Distinguer réalisé net d'avoirs, ferme non facturé et ventes complémentaires estimées.
3. Construire les scénarios sans compter deux fois une même vente.
4. Définir les coûts inclus, calculer les marges puis contrôler formules, totaux et comparabilité.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [references/](references) | Références consultées lorsque le workflow en a besoin. |

### Pour approfondir

- [Structure de suivi](references/modele-suivi.md).
- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une prévision n'est pas du CA engagé. Une marge après coûts partiels n'est pas un bénéfice net. Les taux de conversion et répartitions inconnus ne sont pas inventés ; ils restent des hypothèses à définir.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
