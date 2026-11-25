# Grille d'audit d'un produit existant

Cette grille définit les questions de contrôle, pas une obligation de modifier chaque domaine. Commencer par le parcours essentiel et les risques liés à l'usage. Pour chaque domaine, noter applicabilité, niveau d'examen, sources et limites. « Non applicable » nécessite une raison ; « pas de preuve » signifie généralement « non vérifié ».

| Domaine | Ce qu'il faut confronter | Preuves ou essais utiles |
| --- | --- | --- |
| Besoin et cible | Problème résolu, utilisateurs, fréquence, alternative actuelle, valeur observable | Besoin initial, retours sourcés, exemple de tâche accomplie ; distinguer utilisateur supposé et rencontré |
| Fonctionnalités et complétude | Parcours de bout en bout, droits, états vides, erreurs, annulation, import/export, persistance et reprise | Exigences et scénarios, essais de résultats réels ; distinguer fonction absente, partielle, défectueuse et hors périmètre |
| UX/UI | Compréhension, navigation, hiérarchie, cohérence, feedback, prévention et récupération des erreurs | Captures avec écran, état et version ; parcours observé avec conséquence concrète ; ne pas juger seulement l'esthétique |
| Accessibilité et langues | Clavier, focus, intitulés, contraste, zoom, lecteur d'écran selon outils, formats locaux | Vérifications réelles et limites ; une analyse automatique seule ne prouve pas l'accessibilité |
| Spécifications | Exigences d'origine, décisions suivantes, écarts du produit, critères d'acceptation | Matrice source → exigence → implémentation → vérification ; noter les exigences ambiguës et nouvelles |
| Architecture et maintenabilité | Modules, responsabilités, couplage, flux de données, configuration, dépendances, compromis | Points d'entrée et appels réels, manifests, schéma cohérent avec le code, décisions d'architecture |
| Données et confidentialité | Collecte, stockage, accès, intégrité, export, suppression, rétention, sauvegarde et restauration | Schémas, essais sur données d'essai, configuration réelle ; distinguer politique déclarée et mécanisme présent |
| Sécurité | Authentification et autorisations si présentes, secrets, entrées, dépendances, frontières de confiance | Menaces plausibles dans le contexte, contrôles du code et essais autorisés ; pas de scan intrusif d'un tiers |
| Tests et qualité | Risques couverts, assertions utiles, tests des erreurs, tests d'intégration, E2E, CI et flakiness | Commandes et résultats de la bonne version ; couverture mesurée avec outil/périmètre, distincte de la couverture des exigences |
| Performance et ressources | Latence, mémoire, CPU/GPU, stockage, volume et concurrence pertinents | Mesures dans un environnement et avec un jeu de données précisés ; ne pas inventer de cible de performance |
| Installation et mise à jour | Prérequis, installation propre, chemins, droits, configuration, désinstallation, compatibilité et migration | Essai isolé ou machine cible si disponible ; test sur machine de développement décrit comme tel |
| Livraison et déploiement | Build reproductible, contenu du paquet, versions, migrations, configuration par environnement, retour arrière | Scripts, pipeline, artefact identifié, essai de déploiement autorisé et procédure de restauration ; pas seulement un badge CI |
| Exploitation et support | Logs utiles sans secrets, diagnostic, supervision selon usage, sauvegarde, support et incident | Exemple d'échec et récupération, runbook exécutable ; ne pas imposer une infrastructure à un petit outil local |
| Documentation | Démarrage, guide utilisateur, référence fonctionnelle, architecture, contribution, installation, exploitation | Procédures comparées aux commandes et comportements actuels ; liens et exemples exécutés lorsque possible |
| Distribution, SEO et visibilité | Découvrabilité du dépôt, site, store et canaux ; découvrabilité des pages publiques | Pages réellement publiques, crawl/indexabilité si accessibles, statistiques autorisées et datées ; traiter le site séparément de l'application |
| Offre et vente | Cible acheteuse, bénéfice différenciant, alternatives, prix à tester, coût complet, distribution et support | Retours, demandes, essais ou ventes observés ; hypothèses de prix séparées des données ; pas de prévision de succès sans base |
| Licences et obligations | Origine des assets, licences de dépendances/modèles, redistribution, engagements et obligations pertinentes | Fichiers de licence et sources officielles à jour selon pays/canal ; ce contrôle n'est pas une certification juridique |

## Proportionner la profondeur

- **Outil local personnel** : privilégier fiabilité, installation, données et usage réel. SEO sur l'exécutable : non applicable ; visibilité d'un éventuel site : sujet distinct.
- **Application diffusée** : ajouter compatibilité cible, mises à jour, documentation publique, support et licences de redistribution.
- **Service en ligne** : examiner aussi disponibilité, comptes, isolation des données, déploiements, observabilité et restauration selon le contexte.
- **Produit destiné à la vente** : ajouter validation du besoin payant, canal d'acquisition, offre, coût de service, paiement ou distribution si présents. L'intention de vendre n'oblige pas à créer immédiatement un SaaS.

Les outils avec IA, modèles ou services externes peuvent nécessiter un contrôle du coût d'exécution, des données transmises, du comportement en échec et des droits d'usage. Les contextes réglementés demandent un examen adapté et des sources compétentes ; marquer les points qui dépassent les vérifications disponibles.

## Éviter les conclusions trompeuses

Séparer absence de preuve et preuve d'absence. Une fonctionnalité n'est pas complète parce qu'un bouton existe ; suivre ses entrées, erreurs, effets persistés et sorties utilisables. Une suite verte peut laisser un parcours critique sans test. Un README exhaustif peut décrire des capacités absentes. Une copie déjà fonctionnelle chez le développeur ne prouve pas une installation indépendante.
