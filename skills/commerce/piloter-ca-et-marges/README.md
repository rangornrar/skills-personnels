# Piloter le CA et les marges

## But

Construire un suivi du réalisé, un atterrissage commercial et une analyse des marges par canal ou référence, avec des hypothèses explicites et des calculs actualisables.

## Quand l'utiliser

Pour rapprocher factures, commandes, prospection et exports marketplaces, comparer des périodes ou examiner la rentabilité d'un scénario.

## Informations à fournir

- Période, date d'arrêté, canaux, devise et définition du CA retenue.
- Factures, avoirs, commandes, données de prospection et historiques utiles.
- Prix, volumes, coûts et frais avec unités, assiettes et périodicités ; hypothèses connues.

## Fonctionnement

1. Rapprocher les ventes par clés, séparer leurs états et repérer doublons ou données manquantes.
2. Distinguer réalisé net d'avoirs, ferme non facturé et ventes complémentaires estimées.
3. Construire les scénarios sans compter deux fois une même vente.
4. Définir les coûts inclus, calculer les marges puis contrôler formules, totaux et comparabilité.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Modèle commercial | Sources, rapprochements, hypothèses et synthèse par canal. | Classeur Excel ou autre tableur disponible, si demandé. |
| Atterrissage | Réalisé, ferme, prévision complémentaire et comparatif à périmètre constant. | Tableau de synthèse et scénarios conditionnels. |
| Analyse de marge | Coûts inclus, assiettes, marge de contribution et réserves. | Calculs traçables ; graphiques si utiles. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $piloter-ca-et-marges pour rapprocher ces factures et
commandes puis préparer l'atterrissage de fin d'année par canal.
Sépare les hypothèses de volume et les frais de calcul de marge.
```

## Limites et contrôles

Une prévision n'est pas du CA engagé. Une marge après coûts partiels n'est pas un bénéfice net. Les taux de conversion et répartitions inconnus ne sont pas inventés ; ils restent des hypothèses à définir.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Structure de suivi](references/modele-suivi.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence MIT](../../../LICENSE).
