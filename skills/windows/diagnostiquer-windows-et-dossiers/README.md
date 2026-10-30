# Diagnostiquer Windows et les dossiers

Établir la cause d'un problème Windows ou comparer des arborescences après copie ou clonage, puis proposer une correction justifiée et ciblée.

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

Pour les fichiers, dossiers, disques, permissions ou erreurs d'application. La livraison d'une application depuis son code relève d'un autre skill.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Chemins exacts, symptôme, message d'erreur et résultat attendu.
- Contexte : copie, clonage, synchronisation, ancienne installation ou changement récent.
- Pour une comparaison : sens, exclusions et niveau de preuve recherché.

### Exemple de demande

```text
Utilise $diagnostiquer-windows-et-dossiers pour comparer ces
deux répertoires après clonage. Confirme les différences de contenu
et signale les fichiers illisibles sans modifier les sources.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Diagnostic | Constats, preuves, cause établie ou hypothèses restantes. | Rapport court ou fichier de diagnostic si utile. |
| Comparaison | Fichiers absents, supplémentaires, identiques ou différents, exclusions et erreurs. | Tableau ou rapport exporté selon le besoin. |
| Correction et bilan | Action ciblée, effets observés et retour arrière disponible. | Seulement pour les modifications autorisées ; journal lorsque pertinent. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill diagnostiquer-windows-et-dossiers
python scripts/install_local.py --skill diagnostiquer-windows-et-dossiers --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Identifier les chemins résolus et le rôle des volumes et dossiers concernés.
2. Examiner attributs, droits, propriétaire, liens/jonctions et journaux pertinents sans présumer la cause.
3. Comparer chemins, tailles et dates puis utiliser les empreintes quand l'identité du contenu doit être confirmée.
4. Relier la correction à une cause établie et respecter le périmètre autorisé.
5. Vérifier le résultat après intervention et signaler les fichiers illisibles ou contrôles incomplets.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |

### Pour approfondir

- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Un nom de dossier ne prouve pas son rôle système. Taille et date seules ne prouvent pas l'identité des données. Les jonctions peuvent sortir du périmètre. Aucune suppression récursive ni prise de possession globale n'est faite sur une simple hypothèse.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
