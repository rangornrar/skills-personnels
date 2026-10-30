# Concevoir et améliorer l’UI/UX

Concevoir ou améliorer une interface en reliant les décisions de design aux tâches réelles des utilisateurs, au rendu observé et aux conventions de la plateforme.

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

Pour auditer un parcours, créer une interface, comparer des directions ou implémenter les améliorations demandées sur une application web, mobile ou de bureau.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- Application accessible, captures ou maquettes ; code et documentation lorsque disponibles.
- Utilisateurs, tâches prioritaires, plateforme, contraintes et système de design existant.
- Périmètre attendu : diagnostic, propositions ou modifications à réaliser.

### Exemple de demande

```text
Utilise $concevoir-ameliorer-ui-ux pour auditer le parcours d'export
de cette application Windows. Observe l'interface et propose les
corrections prioritaires avec une façon de les vérifier.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Diagnostic priorisé | Écran ou étape, preuve, effet utilisateur, proposition, priorité et vérification. | Réponse structurée ou tableau. |
| Conception proposée | Parcours, états, libellés, disposition et hypothèses. | Schéma, wireframe ou maquette si utile et réalisable. |
| Modification vérifiée | Changements de code et rendu contrôlé, avec contrôles réalisés et limites. | Fichiers du projet, si l'implémentation est demandée. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill concevoir-ameliorer-ui-ux
python scripts/install_local.py --skill concevoir-ameliorer-ui-ux --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Observer les écrans et le parcours avant de conclure ; distinguer défaut vu, hypothèse à tester et préférence esthétique.
2. Rechercher des références pertinentes pour les changements substantiels et expliquer leurs limites de transposition.
3. Relier chaque constat à son effet utilisateur, une solution précise et une manière de la vérifier.
4. Prioriser et comparer les options utiles ; implémenter puis contrôler le rendu lorsque la demande le prévoit.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |

### Pour approfondir

- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une capture ne prouve pas le bon fonctionnement du clavier ou d'un lecteur d'écran. L'auto-évaluation ne constitue pas un test utilisateur et un contrôle partiel ne démontre pas une conformité globale.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
