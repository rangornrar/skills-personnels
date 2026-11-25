# Besoin, plateforme et architecture

Lire pour cadrer une idée ou prendre une décision qui engage l'implémentation. Ne traiter que les dimensions qui affectent le projet.

## Établir une première version utile

Partir d'un exemple réel : qui déclenche quelle tâche, avec quelles informations, et quel résultat attendu ? Identifier le problème actuel et le bénéfice observable, sans supposer que toute idée de fonctionnalité est nécessaire.

Clarifier progressivement :
- Utilisateurs, rôles éventuels, contexte personnel ou professionnel et appareils réellement utilisés.
- Scénario principal, règles métier, entrées, sorties et erreurs qui empêchent la tâche.
- Première version, exclusions et fonctions ultérieures ; noter la raison d'une exclusion importante.
- Réseau, usage hors ligne, données locales ou partagées, synchronisation et intégrations.
- Contraintes imposées : matériel, OS, accessibilité, confidentialité, compétences, budget, délai et maintenance.
- Diffusion personnelle, équipe, organisation ou grand public ; installation directe, store, navigateur ou autre canal pertinent.

Ne pas inventer de volume, délai, coût, disponibilité ou objectif de performance. Si un adjectif influence l'architecture (« instantané », « sécurisé », « beaucoup »), obtenir un exemple ou proposer une mesure explicite.

Associer à chaque scénario prioritaire un identifiant stable, une priorité, des règles utiles et des critères d'acceptation observables. Exemple : « Après une modification hors ligne, fermer puis relancer l'application conserve le choix effectué. » N'ajouter ce critère que si la persistance hors ligne répond au besoin.

## Décider de la plateforme avant la stack

Une plateforme cible n'est pas un langage. Identifier séparément OS, catégories d'appareils, tailles et modes d'entrée, versions à prendre en charge, puis canal de distribution.

| Cible envisagée | Points discriminants à vérifier selon le produit |
| --- | --- |
| Android | API système et permissions, tâches en arrière-plan, diversité des appareils, stockage, signature et distribution. |
| iOS / iPadOS | API et restrictions de l'OS, chaîne de construction et signature, appareils d'essai, compte de diffusion et canaux autorisés. |
| Windows | Versions et architectures processeur, intégration bureau, droits d'installation, packaging et mise à jour. |
| macOS / Linux | Outils et environnements de construction, formats de distribution, intégration bureau et validation sur les cibles. |
| Web / PWA | Navigateurs et capacités requises, installation éventuelle, accessibilité, stockage, hors ligne, hébergement et exposition réseau. |
| Plusieurs cibles | Réutilisation réellement possible, écarts UX et API, extensions natives, tests et charge de maintenance par cible. |

Vérifier les exigences actuelles dans la documentation officielle de la plateforme et du framework envisagé. Ne pas donner une liste figée d'outils compatibles ou des règles de store de mémoire.

Pour un arbitrage réel, comparer deux ou trois options viables, pas un catalogue de frameworks. Une petite matrice suffit : option, couverture des besoins, obstacle principal, maintenance, prérequis de build et de diffusion. Recommander celle qui sert le mieux le projet et préciser ce qui ferait changer le choix.

Ne pas réduire le multiplateforme à un gain automatique : le code partagé n'élimine ni le packaging ni la validation par OS. Préférer une cible initiale si les autres n'ont pas de besoin établi.

## Poser une architecture réalisable

Décrire seulement les frontières utiles :
- Interface, logique métier, stockage et intégrations ; responsabilités et dépendances.
- Modèle de données, source de vérité, durée de conservation et opérations d'import/export.
- API ou services nécessaires, contrats et comportement si le réseau ou le service échoue.
- Comptes et autorisations si le besoin les exige ; aucun secret confidentiel embarqué dans un client distribué.
- Stratégie hors ligne et conflits de synchronisation si plusieurs copies de données existent.
- Configuration par environnement et chemin de livraison.

Favoriser la solution la plus simple qui satisfait les contraintes. Un schéma textuel ou Mermaid peut expliquer les composants ; ne pas créer des couches pour remplir un modèle.

Pour une décision structurante, consigner contexte, options viables, choix ou recommandation, motif, conséquence et statut. Respecter les décisions antérieures ; rouvrir uniquement si une contrainte ou une preuve change.

## Réduire l'incertitude avant l'effort

Établir une petite matrice : cible, environnement de build, signature, possibilité de test et canal de livraison, avec statut vérifié / disponible / manquant / à confirmer.

Lorsqu'une API système est centrale au produit, faire une preuve ciblée : appel réel, permission accordée ou refusée et résultat sur une cible pertinente. Si le matériel, le SDK ou les accès manquent, expliquer ce que le code ou un simulateur permet d'établir et ce qui reste non prouvé.

Terminer le cadrage quand le scénario prioritaire, sa recette et un chemin de réalisation crédible existent. Les détails réversibles peuvent être affinés pendant l'implémentation ; un objectif métier inconnu ou une capacité centrale non établie reste un point ouvert.
