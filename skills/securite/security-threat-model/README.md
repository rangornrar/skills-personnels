# Modéliser les menaces applicatives

## But

Construire un modèle de menaces spécifique au dépôt et à son déploiement, fondé sur les actifs, entrées, flux et frontières de confiance observés.

## Quand l'utiliser

Sur demande explicite de modélisation des menaces ou d'analyse des chemins d'abus d'un dépôt. Une simple présentation d'architecture ne nécessite pas ce workflow.

## Informations à fournir

- Dépôt ou sous-répertoire dans le périmètre, documentation et code accessibles.
- Usage, déploiement, exposition Internet, sensibilité des données et attentes d'authentification.
- Éléments hors périmètre et hypothèses connues, à préciser lorsqu'ils modifient les priorités.

## Fonctionnement

1. Établir le système à partir de preuves du dépôt et séparer exécution, CI/outillage et exemples.
2. Identifier actifs, points d'entrée, frontières et capacités réalistes des attaquants.
3. Décrire les chemins d'abus et hiérarchiser impact et vraisemblance avec une justification qualitative.
4. Faire confirmer les hypothèses déterminantes puis proposer des mesures liées aux composants concernés.
5. Contrôler couverture, preuves et réserves avant de rédiger le rapport selon le contrat amont.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Modèle du système | Composants, flux, frontières de confiance et preuves dans le dépôt. | Résumé et schéma Mermaid compact. |
| Analyse des menaces | Chemins d'abus, actifs touchés, priorités, mesures existantes et proposées. | Rapport Markdown avec hypothèses et questions ouvertes. |
| Fichier final | Rapport complet au format prévu par le skill. | <nom-du-depot-ou-dossier>-threat-model.md. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $security-threat-model pour ce dépôt et son service
exposé sur Internet. Identifie les entrées et frontières de
confiance, puis prépare les questions de contexte avant le rapport.
```

## Limites et contrôles

Les scénarios de menace ne sont pas automatiquement des vulnérabilités confirmées. Les hypothèses non validées rendent certaines priorités conditionnelles. Le skill ne réalise pas un test d'intrusion ni un déploiement de correctifs. Le guide français est un ajout local à l'import OpenAI.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Contrat du rapport](references/prompt-template.md).
- [Actifs et contrôles](references/security-controls-and-assets.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence Apache 2.0 des fichiers importés](LICENSE.txt). Ce README français est une documentation locale sous [licence MIT](../../../LICENSE).
