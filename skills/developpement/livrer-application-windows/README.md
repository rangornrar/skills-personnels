# Livrer une application Windows

## But

Préparer une livraison Windows vérifiable depuis le dépôt réel du projet, en reliant changements, essais, versions et artefacts.

## Quand l'utiliser

Pour préparer une correction, un build de livraison, un paquet ou une release de SnapSlate, Transcript ou d'une application comparable.

## Informations à fournir

- Dépôt et consignes de projet, branche/commit visé, état des modifications locales.
- Problème corrigé, périmètre et mode de distribution souhaité.
- Outils de build disponibles, architecture cible et procédure de version/signature du projet.

## Fonctionnement

1. Lire les procédures et identifier la stack réelle, les ressources à embarquer et la livraison attendue.
2. Réaliser les changements autorisés et tester le comportement concerné ainsi que les contrôles requis.
3. Compiler et empaqueter avec les versions cohérentes entre application, manifeste, tag et artefact.
4. Contrôler le paquet, rédiger les notes et publier uniquement les étapes externes demandées.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Modifications et validation | Diff, tests effectués, résultats et contrôles encore attendus. | Fichiers du projet et bilan de validation. |
| Paquet | Artefact correspondant à la version, à l'architecture et au mode de distribution. | Format défini par le projet, par exemple MSIX si applicable ; pas de format imposé. |
| Notes de livraison | Problème corrigé, résultat utilisateur, commit, limites et retour arrière utile. | Changelog ou notes de release ; lien GitHub si publication demandée et constatée. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $livrer-application-windows pour préparer le paquet
de cette application et ses notes de livraison. Suis les consignes
du dépôt et distingue tests automatisés et essais manuels.
```

## Limites et contrôles

Un build réussi ne prouve pas le fonctionnement de l'UI. Le skill ne crée pas un certificat ni ne contourne les protections pour débloquer une signature. Préparer une livraison ne vaut pas soumission à un store.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence MIT](../../../LICENSE).
