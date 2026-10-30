# Diagnostiquer Windows et les dossiers

## But

Établir la cause d'un problème Windows ou comparer des arborescences après copie ou clonage, puis proposer une correction justifiée et ciblée.

## Quand l'utiliser

Pour les fichiers, dossiers, disques, permissions ou erreurs d'application. La livraison d'une application depuis son code relève d'un autre skill.

## Informations à fournir

- Chemins exacts, symptôme, message d'erreur et résultat attendu.
- Contexte : copie, clonage, synchronisation, ancienne installation ou changement récent.
- Pour une comparaison : sens, exclusions et niveau de preuve recherché.

## Fonctionnement

1. Identifier les chemins résolus et le rôle des volumes et dossiers concernés.
2. Examiner attributs, droits, propriétaire, liens/jonctions et journaux pertinents sans présumer la cause.
3. Comparer chemins, tailles et dates puis utiliser les empreintes quand l'identité du contenu doit être confirmée.
4. Relier la correction à une cause établie et respecter le périmètre autorisé.
5. Vérifier le résultat après intervention et signaler les fichiers illisibles ou contrôles incomplets.

## Livrables attendus (outputs)

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Diagnostic | Constats, preuves, cause établie ou hypothèses restantes. | Rapport court ou fichier de diagnostic si utile. |
| Comparaison | Fichiers absents, supplémentaires, identiques ou différents, exclusions et erreurs. | Tableau ou rapport exporté selon le besoin. |
| Correction et bilan | Action ciblée, effets observés et retour arrière disponible. | Seulement pour les modifications autorisées ; journal lorsque pertinent. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Exemple de demande

```text
Utilise $diagnostiquer-windows-et-dossiers pour comparer ces
deux répertoires après clonage. Confirme les différences de contenu
et signale les fichiers illisibles sans modifier les sources.
```

## Limites et contrôles

Un nom de dossier ne prouve pas son rôle système. Taille et date seules ne prouvent pas l'identité des données. Les jonctions peuvent sortir du périmètre. Aucune suppression récursive ni prise de possession globale n'est faite sur une simple hypothèse.

## Ressources et installation

- [Instructions de référence](SKILL.md).
- [Installation dans la bibliothèque et sur ChatGPT](../../../README.md#installer-les-skills-utiles).
- [Catalogue général](../../../CATALOGUE.md).
- [Licence MIT](../../../LICENSE).
