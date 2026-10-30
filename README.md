# Skills personnels

[![Validation](https://github.com/rangornrar/skills-personnels/actions/workflows/validate.yml/badge.svg)](https://github.com/rangornrar/skills-personnels/actions/workflows/validate.yml)
[![Licence des créations : MIT](https://img.shields.io/badge/créations-MIT-green.svg)](LICENSE)

**Une bibliothèque de 18 skills classés par genre : 11 nouveaux workflows en français, 3 skills existants et 4 compléments officiels OpenAI.**

Les skills portent les méthodes de travail et critères de qualité. Les logiciels, moteurs d'image, connecteurs et outils de production restent ceux disponibles dans l'environnement d'exécution.

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

## Installer les skills utiles

Le classement par genre appartient au dépôt. À l'installation, chaque dossier de skill est placé directement dans le répertoire de découverte du client ; ne pas copier uniquement les fichiers `SKILL.md`.

### Avec le skill-installer

Demander dans Codex :

```text
Utilise $skill-installer pour installer depuis rangornrar/skills-personnels
le skill situé dans skills/photo-et-visuels/preparer-seance-photo.
```

L'accès au dépôt privé nécessite un compte autorisé. Les chemins exacts figurent dans le catalogue.

### Depuis une copie locale

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

## Utiliser

```text
Utilise $preparer-seance-photo pour préparer cette séance et son livret de poses.
Utilise $preparer-fiches-marketplaces pour préparer cette référence à partir des sources jointes.
Utilise $transcrire-reunion-et-actions pour produire le compte rendu de cette transcription.
```

L'invocation implicite reste disponible pour les skills personnels. Les imports OpenAI conservent leurs instructions et métadonnées d'origine. Leur langue de rédaction peut rester l'anglais ; demander une restitution en français si nécessaire.

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
