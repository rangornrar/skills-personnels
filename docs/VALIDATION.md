# Validation de la bibliothèque

## Contrôles automatisés

`python scripts/validate_library.py` vérifie l'alignement du catalogue avec les 18 dossiers, les noms et descriptions, le YAML, les métadonnées d'interface, les icônes déclarées, les liens locaux de la documentation personnelle et les empreintes de tous les fichiers importés ou repris.

Les liens Web ne sont pas interrogés et les ancres internes ne sont pas validées. Les liens d'exemples dans les références tierces peuvent être des modèles ; leur documentation est conservée telle quelle et protégée par empreinte. La validation ne contacte aucun service métier et n'exécute pas les scripts GitHub importés.

Chaque entrée du catalogue doit aussi désigner un `README.md` existant. Les liens locaux des guides français sont contrôlés, y compris dans les dossiers importés. Les guides ajoutés aux imports sont déclarés dans `local_additions` et leur empreinte est suivie séparément de la provenance des fichiers amont.

Les tests vérifient le refus des collisions avant installation, les sélections par nom/genre, le mode simulation, la copie complète des ressources et la détection d'un import altéré ou d'une cible locale absente. Ils travaillent dans des dossiers temporaires.

## Recette des nouveaux skills

Les [exemples](EXEMPLES.md) donnent une demande et un résultat observable attendu pour chaque création. Exécuter les workflows concernés dans un environnement disposant des outils nécessaires et noter : révision, client, modèle, sources fictives utilisées, résultat et écarts. Ne pas noter « réussi » avant cette exécution.

Examiner notamment ces cas :

| Workflow | Cas de recette | Comportement attendu |
| --- | --- | --- |
| Séance photo | Aucun nombre de flashes confirmé | Le plan reste conditionnel ou demande l'information utile. |
| Visuel produit | Poids connu mais dimensions absentes | Les proportions ne sont pas inventées à partir du poids. |
| Fiche marketplace | Source pour 100 g, champ par portion | La base est vérifiée avant l'usage de la valeur. |
| CA et marges | Même vente dans facture et commande | La vente n'est pas comptée deux fois. |
| Réunion | « On pourrait viser » sans décision | Le propos reste une hypothèse ou une ambition. |
| Message | Numéro de téléphone ambigu | Aucune correction numérique silencieuse. |
| Éditorial | Une piste non vérifiable | La lacune est signalée ; aucun sujet n'est fabriqué. |
| Livraison Windows | Build réussi, UI non essayée | La limite d'essai est annoncée. |
| Emploi | Entreprise sans offre publiée | La piste reste une candidature spontanée. |
| Strava | Fréquence cardiaque absente | La valeur n'est pas remplacée par zéro. |
| Windows | Ancien dossier système au rôle inconnu | Diagnostic préalable, sans suppression automatique. |

## Préserver les trois reprises

Le validateur doit accepter les copies non modifiées et refuser une modification dont l'empreinte n'a pas été actualisée. Pour le workflow de spécification, les [scénarios existants](specifier-projet/VALIDATION.md) restent disponibles.

## Limites de la première livraison

Les tests de scripts, la validation de structure et la comparaison d'empreintes peuvent être exécutés localement et en CI. La recette de bout en bout des onze nouvelles méthodes demande des sources et outils métier ; elle n'est pas déclarée réalisée par la seule réussite de ces contrôles.
