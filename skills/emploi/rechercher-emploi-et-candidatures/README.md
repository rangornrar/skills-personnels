# Rechercher un emploi et candidater

Organiser une recherche d'emploi à partir d'un parcours réel, trouver des pistes vérifiables et préparer des candidatures adaptées avec un suivi clair.

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

Pour une recherche locale ou ciblée, l'adaptation d'un CV/message et le suivi des candidatures. Le workflow accompagne le candidat et ne sélectionne pas des personnes pour un recruteur.

## Comment l'utiliser

Décrire la tâche et le résultat souhaité, puis fournir les éléments ci-dessous. Adapter l'exemple au contexte réel.

### Informations à fournir

- CV et expériences établies ; fonctions recherchées et compétences démontrées.
- Zone, mode de transport, temps de trajet, contrat et autres contraintes exprimées.
- Offres ou entreprises déjà repérées, candidatures envoyées et formats attendus.

### Exemple de demande

```text
Utilise $rechercher-emploi-et-candidatures pour ce CV. Recherche
des pistes dans la zone indiquée, distingue les annonces ouvertes
des candidatures spontanées et prépare un tableau de suivi.
```

## Sorties attendues

| Livrable | Contenu | Format et condition |
| --- | --- | --- |
| Pistes qualifiées | Entreprise, poste ou type de piste, lieu, source et date de vérification. | Liste ou tableau avec adéquation et réserves. |
| Candidature adaptée | CV et message fondés sur le parcours réel. | Texte ou document mis en page si demandé et réalisable. |
| Suivi | Statut, dates, sources et relances demandées. | Tableau ou fichier Excel selon le besoin. |

Les formats de fichiers dépendent des outils disponibles. Les fichiers annoncés doivent avoir été réellement créés ; un format facultatif n'est pas un livrable garanti.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles) pour choisir la méthode adaptée : ChatGPT sur le site web, skill-installer de Codex ou copie locale.

Depuis la racine d'une copie locale de la bibliothèque :

```sh
python scripts/install_local.py --skill rechercher-emploi-et-candidatures
python scripts/install_local.py --skill rechercher-emploi-et-candidatures --apply
```

La première commande affiche les copies prévues ; la seconde les effectue. Un dossier déjà présent n'est pas écrasé.

## Fonctionnement détaillé

1. Lire le profil et clarifier les critères qui changent la sélection.
2. Ouvrir les annonces actuelles et distinguer postes ouverts, pistes à revalider et candidatures spontanées.
3. Relier l'adéquation aux exigences du poste et signaler les points à confirmer.
4. Adapter les documents sans inventer d'expérience puis dédupliquer et organiser le suivi.

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |

### Pour approfondir

- [Catalogue général](../../../CATALOGUE.md).

## Limites et contrôles

Une entreprise cible n'est pas nécessairement un poste ouvert. Une distance ne confirme pas un temps de trajet aux horaires réels. La préparation ne vaut pas autorisation d'envoyer le CV ou de le publier en CVthèque.

## Licence

Documentation locale sous [licence MIT](../../../LICENSE).
