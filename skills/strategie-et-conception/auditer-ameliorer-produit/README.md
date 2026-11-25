# Auditer et améliorer un produit existant

Revoir un logiciel déjà créé, corriger les écarts demandés et préparer sa suite avec un rapport PDF, des preuves et un plan d'actions. Le skill s'applique aux outils locaux, applications distribuées et services web, en adaptant les contrôles au contexte.

## Sommaire

- [À quoi cela sert](#à-quoi-cela-sert)
- [Comment l'utiliser](#comment-lutiliser)
- [Sorties attendues](#sorties-attendues)
- [Fonctionnement](#fonctionnement)
- [Installation](#installation)
- [Architecture et ressources](#architecture-et-ressources)
- [Limites](#limites)

## À quoi cela sert

Déterminer ce qui fonctionne, ce qui manque, ce qui doit être corrigé et ce qui permettrait de diffuser ou vendre l'outil. La revue couvre :

- UX/UI, accessibilité, usages, fonctionnalités et complétude des parcours.
- Comparaison avec les spécifications initiales, évolutions et décisions.
- Architecture, code, données, sécurité, performances et maintenabilité.
- Tests, installation, mise à jour, livraison, déploiement et exploitation.
- Documentation utilisateur, technique et d'architecture.
- Distribution, site de présentation, SEO, visibilité, offre et possibilité de vente.
- Licences, support, coûts et autres enjeux pertinents selon le produit.

Tous les domaines ne s'appliquent pas à tous les outils. Le rapport distingue ce qui a été examiné, ce qui reste à vérifier et ce qui n'est pas pertinent. Il ne transforme pas automatiquement un outil personnel en produit commercial.

## Comment l'utiliser

Fournir le dossier ou dépôt, l'URL si pertinente et les documents de départ accessibles. Ajouter l'objectif : usage personnel, diffusion gratuite, vente ou remise à niveau avant livraison. Le skill commence par les sources disponibles ; il demande seulement les informations qui peuvent modifier le diagnostic.

**Audit et corrections**

```text
Utilise $auditer-ameliorer-produit sur [dossier ou dépôt].
Reprends les spécifications initiales, audite le produit de bout en bout,
corrige les problèmes dans le périmètre établi et mets à jour la documentation.
Produis le rapport PDF avant/après et un plan pour diffuser ou vendre l'outil.
```

**Audit sans modification du produit**

```text
Utilise $auditer-ameliorer-produit sur [produit].
Fais l'audit et le PDF sans modifier l'application ni ses documents.
Classe les corrections et les prochaines décisions.
```

**Reprise**

```text
Utilise $auditer-ameliorer-produit pour reprendre [dossier d'audit].
Vérifie les corrections depuis la dernière version, actualise les statuts
et le PDF, puis prépare le prochain lot d'actions.
```

Une application locale peut avoir besoin d'un site de présentation ; le skill examine cette possibilité sans prétendre auditer un site qui n'existe pas.

## Sorties attendues

| Sortie | Contenu |
| --- | --- |
| Rapport PDF et source éditable | Diagnostic initial, constats, changements réels, contrôles et recommandations |
| Registre des constats | Preuves, conséquences, gravité et suivi de chaque écart |
| Matrice des exigences | Besoins initiaux, réalisation observée, tests et décisions |
| Documentation actualisée | Guides et spécifications concernés, si leur modification est demandée |
| Correctifs | Changements locaux autorisés avec vérifications, si demandés |
| Plan de suite | Dépendances, livrables, critères de réussite : livraison, site, mise en ligne, SEO, acquisition ou test de vente selon contexte |

Le dossier conserve ce qui est réalisé, vérifié, bloqué ou différé. Une possibilité de vente est une hypothèse argumentée à tester ; le skill ne promet ni clients ni chiffre d'affaires.

## Fonctionnement

Le skill fige d'abord un état initial, examine les domaines applicables et confronte les constats sous plusieurs regards. Il relie ensuite les corrections demandées aux exigences et aux vérifications. Il produit enfin le PDF et les prochaines actions, en conservant les limites d'accès et les décisions ouvertes.

Les documents historiques restent identifiables. Si les spécifications initiales manquent, une reconstruction est présentée comme telle. Les changements proposés ne deviennent pas des besoins approuvés par simple réécriture de la documentation.

Les autres skills disponibles peuvent approfondir l'UI/UX, les besoins, la sécurité ou la livraison. Ce skill conserve la synthèse et la traçabilité ; leur installation n'est pas nécessaire pour lire ses propres instructions.

## Installation

Suivre le [guide général](../../../README.md#installer-les-skills-utiles) pour Codex ou l'utilisation dans un projet ChatGPT sur le site web.

Depuis la racine de la bibliothèque :

```sh
python scripts/install_local.py --skill auditer-ameliorer-produit
python scripts/install_local.py --skill auditer-ameliorer-produit --apply
```

L'installateur refuse les collisions. Copier le dossier entier, avec ses références et modèles, plutôt que le seul `SKILL.md`.

## Architecture et ressources

| Ressource | Utilité |
| --- | --- |
| [SKILL.md](SKILL.md) | Cadrage, diagnostic, arbitrage, corrections et remise du dossier |
| [Grille d'audit](references/grille-audit.md) | Domaines, preuves attendues et adaptation au type de produit |
| [Corrections et documentation](references/corrections-documentation.md) | Traçabilité, mise à niveau et préservation des besoins initiaux |
| [Visibilité et commercialisation](references/visibilite-commercialisation.md) | SEO applicable, distribution, hypothèses de vente et expériences |
| [Rapport et livrables](references/rapport-livrables.md) | Structure du PDF, vérification du rendu et suivi |
| [Registre](assets/registre-constats.csv), [exigences](assets/matrice-exigences.csv), [actions](assets/plan-actions.csv) | En-têtes de tableaux pour reprendre le travail |

Il s'agit d'un skill principal avec des références chargées selon le besoin. Ce découpage évite d'installer un skill pour chaque domaine et de maintenir plusieurs registres concurrents.

## Limites

Un accès au code ne remplace pas l'observation de l'interface ou un essai d'installation. Une couverture de code ne démontre pas la couverture des besoins. Les tests, recherches et rendus réellement effectués restent explicités.

Le PDF et les corrections exigent les outils adaptés et un accès suffisant au projet. Si un contrôle ou une génération est impossible, la limite et la manière de terminer restent indiquées. L'audit ne constitue pas une certification de sécurité, d'accessibilité ou de conformité juridique.

La mise en ligne, les achats, les campagnes et les publications suivent la demande et les autorisations de l'utilisateur ; préparer une action ne signifie pas qu'elle est exécutée.

Création sous licence MIT, comme les autres créations de cette bibliothèque.
