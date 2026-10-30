# Skills personnels

[![Validation](https://github.com/rangornrar/skills-personnels/actions/workflows/validate.yml/badge.svg)](https://github.com/rangornrar/skills-personnels/actions/workflows/validate.yml)
[![Licence des créations : MIT](https://img.shields.io/badge/créations-MIT-green.svg)](LICENSE)

**Une bibliothèque de 18 skills classés par genre : 11 nouveaux workflows en français, 3 skills existants et 4 compléments officiels OpenAI.**

Les skills portent les méthodes de travail et critères de qualité. Les logiciels, moteurs d'image, connecteurs et outils de production restent ceux disponibles dans l'environnement d'exécution.

## Sommaire

- [À quoi sert cette bibliothèque](#à-quoi-sert-cette-bibliothèque)
- [Comment les utiliser](#comment-les-utiliser)
- [Sorties attendues](#sorties-attendues)
- [Parcourir la bibliothèque](#parcourir-la-bibliothèque)
- [Installer les skills utiles](#installer-les-skills-utiles)
- [Architecture de la bibliothèque](#architecture-de-la-bibliothèque)
- [Capacités nécessaires](#capacités-nécessaires)
- [Qualité et maintenance](#qualité-et-maintenance)
- [Sources et licences](#sources-et-licences)

## À quoi sert cette bibliothèque

Réutiliser des méthodes de travail pour des tâches qui reviennent : préparer une séance, rédiger une fiche produit, rendre compte d'une réunion, cadrer un logiciel ou analyser des données. Chaque skill décrit les éléments nécessaires, les étapes utiles et le résultat attendu.

## Comment les utiliser

1. Choisir un workflow dans le [catalogue](CATALOGUE.md) et lire son README.
2. Préparer les fichiers, références et contraintes indiqués dans ce guide.
3. Formuler le résultat attendu et utiliser une demande adaptée à votre contexte.
4. Examiner les sorties et les points encore à confirmer avant de les utiliser.

### Exemples de demandes

```text
Utilise $preparer-seance-photo pour préparer cette séance et son livret de poses.
Utilise $preparer-fiches-marketplaces pour préparer cette référence à partir des sources jointes.
Utilise $transcrire-reunion-et-actions pour produire le compte rendu de cette transcription.
```

L'invocation implicite reste disponible pour les skills personnels. Les imports OpenAI conservent leurs instructions et métadonnées d'origine. Leur langue de rédaction peut rester l'anglais ; demander une restitution en français si nécessaire.

## Sorties attendues

Chaque README décrit les livrables propres au skill et leurs conditions. Voici les principaux types de résultats :

| Usage | Sorties possibles |
| --- | --- |
| Décision et conception | Recommandation, comparaison, spécifications, audit ou proposition d'interface. |
| Photo et visuels | Brief, poses classées, plan d'éclairage, moodboard, livret ou images produits. |
| Commerce | Textes de fiche, attributs sourcés, suivi du CA, scénarios et calculs de marge. |
| Réunions et éditorial | Transcription, compte rendu, actions, message, script ou pack de publication. |
| Développement et sécurité | Diagnostic, correctifs autorisés, paquet, notes de livraison ou rapport de sécurité. |
| Emploi, sport et Windows | Pistes et suivi de candidatures, graphiques d'activités ou rapport de diagnostic. |

Les fichiers, formats et opérations externes dépendent de la demande et des outils disponibles. Un PDF, une vidéo, une publication ou un paquet ne sont annoncés comme réalisés qu'après leur production ou vérification.

## Parcourir la bibliothèque

| Genre | Contenu | Nombre |
| --- | --- | ---: |
| [Stratégie et conception](skills/strategie-et-conception) | Analyse critique, spécifications et UI/UX | 3 |
| [Photo et visuels](skills/photo-et-visuels) | Séances, moodboards et visuels produits | 2 |
| [Commerce](skills/commerce) | Fiches marketplaces, chiffre d'affaires et marges | 2 |
| [Communication et éditorial](skills/communication-et-editorial) | Réunions, messages et contenus sourcés | 3 |
| [Développement](skills/developpement) | Livraison Windows et workflows GitHub | 3 |
| [Sécurité](skills/securite) | Revue de pratiques et modélisation des menaces | 2 |
| [Emploi](skills/emploi) | Recherche, candidatures et suivi | 1 |
| [Sport](skills/sport) | Analyse des exports Strava | 1 |
| [Windows](skills/windows) | Diagnostic et comparaison de dossiers | 1 |

Consulter le [catalogue détaillé](CATALOGUE.md), les [exemples d'utilisation](docs/EXEMPLES.md) ou le [catalogue JSON](catalogue.json) pour choisir un skill.

Chaque skill possède un `README.md` qui explique son but, les informations à fournir, son fonctionnement et ses livrables attendus, avec un exemple et les limites utiles. Les liens du catalogue ouvrent ces guides ; les instructions de référence restent dans `SKILL.md`.

## Installer les skills utiles

Choisir la méthode adaptée : [ChatGPT sur le site web](#sur-chatgpt-site-web), installation par le skill-installer dans Codex ou copie locale.

### Sur ChatGPT (site web)

**Utilisation immédiate dans un projet ChatGPT**

Cette méthode permet de réutiliser les consignes de la bibliothèque dans le navigateur :

1. Sur GitHub, télécharger le dépôt avec **Code → Download ZIP**, puis décompresser l'archive.
2. Choisir un skill dans le [catalogue](CATALOGUE.md), par exemple `skills/photo-et-visuels/preparer-seance-photo/`.
3. Sur [ChatGPT](https://chatgpt.com/), créer ou ouvrir un projet dédié à ce workflow.
4. Ajouter aux sources du projet le fichier `SKILL.md` du skill choisi et ses références utiles, ainsi que les documents nécessaires à la tâche. Un projet par workflow évite les confusions entre plusieurs fichiers nommés `SKILL.md`.
5. Dans les instructions du projet, ajouter :

   ```text
   Pour les demandes relevant de ce workflow, lis le fichier SKILL.md fourni
   et applique ses consignes. Consulte les références jointes lorsqu'elles
   sont utiles. Signale les fichiers ou outils manquants.
   ```

6. Démarrer une conversation dans ce projet, par exemple : « Applique le workflow preparer-seance-photo pour préparer cette séance et son livret. »

Les [projets ChatGPT](https://learn.chatgpt.com/docs/projects) partagent leurs fichiers et instructions entre leurs conversations. Cette utilisation comme consignes de projet ne crée pas une installation native avec sélection du skill par `@`.

**Installation native sur le site, par plugin**

La [documentation officielle des skills](https://learn.chatgpt.com/docs/build-skills) décrit leur distribution sur ChatGPT web dans des plugins. Le dépôt actuel contient les dossiers de skills et leur installateur local ; un package de plugin reste à préparer et à rendre disponible avant une installation native de cette bibliothèque sur le site.

Une fois ce plugin disponible pour votre compte :

1. Ouvrir l'onglet **Plugins** de ChatGPT et retrouver le plugin dans le catalogue ou dans les plugins personnels/de l'espace de travail.
2. Ouvrir sa fiche et sélectionner le bouton **+** pour l'installer.
3. Démarrer une nouvelle conversation, puis utiliser `@` pour sélectionner le plugin ou l'un de ses skills.

Voir la [procédure officielle d'installation des plugins](https://learn.chatgpt.com/docs/plugins). Pour un espace de travail géré, l'[import depuis GitHub](https://learn.chatgpt.com/docs/enterprise/plugin-management) nécessite un administrateur et un manifeste de marketplace compatible, absent de ce dépôt à ce stade.

Sur le site, les capacités dépendent des outils disponibles dans ChatGPT. Ajouter les fichiers d'un skill ne donne pas accès aux dossiers du PC, à ComfyUI ou à GitHub CLI ; les workflows nécessitant ces outils demandent un environnement adapté.

### Dans Codex, avec le skill-installer

Demander dans Codex :

```text
Utilise $skill-installer pour installer depuis rangornrar/skills-personnels
le skill situé dans skills/photo-et-visuels/preparer-seance-photo.
```

L'accès au dépôt privé nécessite un compte autorisé. Les chemins exacts figurent dans le catalogue.

### Dans Codex, depuis une copie locale

Le classement par genre appartient au dépôt. Pour l'installation locale, chaque dossier de skill est placé directement dans le répertoire de découverte du client ; ne pas copier uniquement les fichiers `SKILL.md`.

Après clonage ou téléchargement du dépôt, Python 3.10 ou plus récent suffit pour l'installation locale. Depuis sa racine :

```sh
python scripts/install_local.py --list
python scripts/install_local.py --skill preparer-seance-photo
python scripts/install_local.py --skill preparer-seance-photo --apply
```

Sans `--apply`, le script affiche seulement les copies prévues. Par défaut, la destination est `~/.agents/skills`. Utiliser `--dest` pour un autre emplacement, par exemple le `.agents/skills` d'un projet ou un répertoire de skills déjà configuré dans le client.

```sh
python scripts/install_local.py --genre commerce --apply
python scripts/install_local.py --all
```

Le script refuse toute collision de nom ; il ne remplace pas une installation existante. Si les trois anciens skills sont déjà installés, sélectionner les nouveaux ou les genres voulus. Avant de remplacer une ancienne copie, conserver ses modifications et choisir quelle version fait référence.

Les emplacements locaux suivent la [documentation officielle OpenAI](https://learn.chatgpt.com/docs/build-skills). Certains clients disposent de leur propre importeur. Codex détecte les changements ; redémarrer le client si le skill n'apparaît pas.

## Architecture de la bibliothèque

Le dépôt organise les skills par genre, puis par dossier autonome. Le classement sert à parcourir la bibliothèque ; l'installateur copie les dossiers de skills sélectionnés dans la destination choisie.

| Élément | Rôle |
| --- | --- |
| [skills/](skills) | Genres et dossiers de skills avec README, instructions et ressources. |
| [catalogue.json](catalogue.json) | Noms, chemins, origine et métadonnées de la bibliothèque. |
| [CATALOGUE.md](CATALOGUE.md) | Navigation vers les guides des skills. |
| [docs/](docs) | Exemples, recette et guides complémentaires. |
| [scripts/](scripts) | Installation locale et validation de la bibliothèque. |
| [tests/](tests) | Vérification des scripts et des invariants de la bibliothèque. |
| [sources.lock.json](sources.lock.json) | Empreintes des reprises, imports et documentations locales déclarées. |

## Capacités nécessaires

- **Documents et médias** : les workflows utilisent les outils PDF, DOCX, tableur, image, audio ou vidéo effectivement disponibles. Le dépôt n'embarque ni moteur de transcription ni modèle de génération d'image.
- **Données commerciales** : fournir les sources et modèles du canal ; les règles actuelles sont vérifiées pendant la tâche.
- **GitHub** : `gh-fix-ci` et `gh-address-comments` nécessitent GitHub CLI (`gh`) authentifié. Aucun identifiant n'est fourni dans ce dépôt.
- **Sécurité** : `security-best-practices` vise Python, JavaScript/TypeScript et Go. Les imports décrivent leurs déclencheurs et leur périmètre exacts.
- **Applications Windows** : les outils de compilation et distribution sont définis par chaque projet, pas installés automatiquement par le skill.

## Qualité et maintenance

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_library.py
python -m unittest discover -s tests -v
```

Le contrôle vérifie catalogue, structure, frontmatter, métadonnées, ressources locales et empreintes des imports. GitHub Actions exécute aussi les tests des scripts d'installation et de validation.

Les 11 créations sont des premières versions. Les contrôles statiques ne constituent pas une recette complète des workflows, ni une certification médicale, juridique ou financière. Voir [la méthode de validation](docs/VALIDATION.md) et [le guide de contribution](CONTRIBUTING.md).

## Sources et licences

Les créations et ressources originales de cette bibliothèque sont sous [licence MIT](LICENSE), conformément au choix de l'auteur. Les quatre imports OpenAI conservent leurs fichiers `LICENSE.txt` sous Apache 2.0 et leurs avis. Les [attributions](THIRD_PARTY_NOTICES.md) et [empreintes des sources](sources.lock.json) indiquent leur origine et leur révision.

Les anciens dépôts individuels restent des sources historiques ; cette bibliothèque regroupe les copies de référence indiquées dans le catalogue. Les données de projets réels et les livrables clients restent hors de la bibliothèque.
