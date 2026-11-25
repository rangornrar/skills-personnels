# Créer et déployer des applications

Accompagner une application du besoin à la livraison : choix de plateforme, architecture, maquettes, développement, vérification et déploiement demandé.

## Utilisation

Fournir le problème à résoudre, les utilisateurs, les appareils ou plateformes prioritaires, les contraintes et les fichiers du projet s’il existe. Le workflow reprend au premier point incertain et conserve les décisions déjà prises.

```text
Utilise $creer-deployer-applications pour réaliser cet outil.
Commence par les usages et les plateformes pertinentes, puis construis
une première tranche utilisable avec ses vérifications et sa livraison.
```

## Sorties attendues

- Besoin et critères de réussite, plateforme et architecture motivées.
- Parcours, maquettes consultables et états essentiels.
- Code et première tranche utilisable, puis fonctions prioritaires.
- Vérifications avec distinction entre automatique, émulateur et appareil.
- Artefact ou déploiement demandé, documentation et état de reprise.

Le périmètre suit la demande : des maquettes seules ne déclenchent pas un développement complet. Un aperçu navigateur ne valide pas une API native. Signature, stores, hébergement et déploiement dépendent des accès et outils disponibles ; aucun résultat inaccessible n’est annoncé comme réalisé.

## Installation

Voir le [guide de la bibliothèque](../../../README.md#installer-les-skills-utiles).

```sh
python scripts/install_local.py --skill creer-deployer-applications
python scripts/install_local.py --skill creer-deployer-applications --apply
```

La première commande simule la copie ; la seconde l’effectue. Un dossier existant n’est pas écrasé.

## Ressources

| Fichier | Utilité |
| --- | --- |
| [SKILL.md](SKILL.md) | Consignes et déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Métadonnées et invite. |
| [Cadrage et architecture](references/cadrage-architecture.md) | Besoin, plateformes et faisabilité. |
| [Maquettes et réalisation](references/maquettes-realisation.md) | Prototype, réalisation et vérification. |
| [Livraison et exploitation](references/livraison-exploitation.md) | Distribution et maintenance. |
| [Suivi du projet](references/suivi-projet.md) | Décisions, preuves et reprise. |

## Licence

Skill et documentation sous [licence MIT](../../../LICENSE).
