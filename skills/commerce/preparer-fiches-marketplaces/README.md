# Préparer des fiches marketplaces

## But

Préparer une fiche Amazon, Cdiscount ou autre marketplace à partir de données produit traçables, en séparant contenu éditorial, attributs et offre vendeur.

## Quand l'utiliser

Pour rédiger un listing, compléter un fichier d'import, vérifier des données nutritionnelles ou examiner une erreur de catalogue.

## Informations à fournir

- Canal et pays, catégorie, référence, SKU et identifiants EAN/GTIN ou ASIN disponibles.
- Fiches fournisseur, étiquettes, composition, quantités, unités et données nutritionnelles sourcées.
- Modèle d'import ou champs à remplir ; pour une erreur, message complet et contexte.

## Fonctionnement

1. Rapprocher les sources, variantes et identifiants puis relever contradictions et lacunes.
2. Vérifier les règles actuelles du canal lorsqu'elles modifient les champs ou contenus attendus.
3. Rédiger titre, puces et description en conservant les caractéristiques établies.
4. Contrôler unités, base nutritionnelle et calculs, puis préparer les données dans le modèle demandé.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Textes prêts à copier | Titre, puces et description adaptés au produit et au canal. | Texte structuré. |
| Table d'attributs | Valeurs, sources, unités, bases de calcul et statuts à confirmer. | Tableau, Excel ou CSV selon la demande et les capacités disponibles. |
| Points bloquants | Données absentes, erreurs à traiter et vérifications avant import. | Liste de contrôle avec réserves. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $preparer-fiches-marketplaces pour préparer la fiche de
ce coffret. Rédige les contenus et une table des attributs sourcés ;
vérifie la base nutritionnelle avant de proposer les valeurs.
```

## Limites et contrôles

Une moyenne calculée pour 100 g ne peut pas être copiée dans un champ par portion sans correspondance vérifiée. Le skill ne fabrique ni composition ni allégation. La préparation d'une fiche n'autorise pas sa publication.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Données et calculs](references/donnees-et-calculs.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence MIT](../../../LICENSE).
