---
name: concevoir-ameliorer-ui-ux
description: "Concevoir, auditer ou améliorer une UX/UI professionnelle et innovante pour Windows, Android, iOS/iPadOS et le web : parcours, recherche actuelle, direction artistique, prototypes et vérification. Utiliser pour une création d'interface, une refonte, un audit ergonomique, un benchmark ou une amélioration visuelle ; implémenter lorsque demandé. Ne pas déclencher pour une correction technique sans enjeu d'interface ni pour un simple visuel marketing."
---

# Concevoir une UX/UI professionnelle et innovante

Répondre en français sauf demande contraire. Viser une interface aboutie, reconnaissable et efficace, avec une direction professionnelle et une signature visuelle affirmée par défaut. Ajuster l'expressivité au public, à l'usage et à la marque. Relier chaque décision importante à la tâche, aux conventions de la plateforme et à une vérification possible. Adapter l'effort au périmètre : une correction locale reste locale.

## Choisir le périmètre et les références utiles

- Déterminer s'il faut conseiller, auditer, explorer, prototyper ou implémenter. Une demande de propositions autorise des propositions ; une demande de modification inclut la réalisation et les vérifications appropriées dans le périmètre autorisé.
- Lire les consignes du projet, les composants et les styles existants. Identifier utilisateurs, tâches, expertise, contenus, plateformes et versions ciblées, framework, modes d'entrée et contraintes connues. Déduire ce qui est accessible ; poser seulement les questions dont la réponse change sensiblement la conception et avancer sur le reste.
- Retenir un critère de réussite observable : retrouver une commande, accomplir une tâche, corriger une erreur, reprendre le travail ou utiliser le parcours au clavier. Sans mesure initiale, proposer comment l'établir sans inventer de gain.
- Lire la section correspondant à la plateforme dans [references/plateformes.md](references/plateformes.md) pour toute décision dépendante de son environnement. Pour un produit multiplateforme, lire les sections concernées.
- Lire [references/direction-artistique.md](references/direction-artistique.md) pour une création, une refonte visuelle ou une exploration substantielle.
- Lire [references/verification.md](references/verification.md) pour un audit, un prototype interactif ou une implémentation ; sélectionner les contrôles affectés par la demande.

## Observer les usages et le parcours

Pour un produit existant, examiner l'interface réelle lorsqu'elle est accessible : capturer les écrans et parcourir la tâche du point d'entrée au résultat avant de conclure. Le code complète l'observation du rendu. Si l'exécution est impossible, exploiter les fichiers ou captures en précisant ce qu'ils permettent d'établir. Une image ne démontre pas le fonctionnement du clavier ou d'un lecteur d'écran.

Pour une création, établir le scénario principal, les informations nécessaires et les actions avant la composition détaillée. Utiliser des contenus représentatifs : intitulés longs, valeurs plausibles, volumes et cas difficiles pertinents. Prévoir les états qui affectent le parcours : premier usage, données absentes ou présentes, attente, erreur, réussite, annulation et reprise.

Distinguer dans le raisonnement :

- **Exigence du référentiel retenu** : citer le critère et son périmètre lorsqu'il fonde une correction.
- **Convention de plateforme** : expliquer l'attente utilisateur et les conséquences d'un écart.
- **Principe ergonomique** : appliquer selon les tâches et le public ; une heuristique oriente l'analyse sans prouver une difficulté observée.
- **Choix artistique ou hypothèse** : préciser l'intention et la manière de l'évaluer.

Ne pas présenter les « lois UX », le nombre de clics ou une préférence visuelle comme une preuve universelle. Une interface experte peut bénéficier d'une densité élevée, d'actions groupées et de raccourcis. Préserver les fonctions utiles et la possibilité de récupérer une erreur ; écarter les interactions trompeuses.

## Rechercher les possibilités actuelles

Effectuer une recherche externe ciblée pour une création, un audit ou une évolution substantielle, et pour une demande de nouveautés. Réutiliser les sources déjà vérifiées dans la session si elles restent pertinentes. Une correction ponctuelle établie ne requiert pas un benchmark complet.

1. Rechercher les recommandations officielles et les capacités disponibles pour les versions du système, du navigateur et du framework ciblées. Ouvrir les pages utiles et vérifier leur portée ; une annonce ne prouve pas la disponibilité dans le projet.
2. Examiner quelques produits comparables par leurs tâches, public et modes d'entrée. Identifier ce qui est testé directement, montré dans une démonstration, visible sur une capture marketing ou seulement décrit. Utiliser les galeries visuelles comme inspiration, avec une recherche distincte de preuves d'usage.
3. Pour les nouveautés pertinentes, noter **source et date de consultation | problème ou intention | disponibilité et versions | statut stable, expérimental ou piste visuelle | coût et limites | solution de repli**. Chercher au-delà des effets décoratifs : capacités d'interaction, d'adaptation, d'accessibilité et de présentation des données.
4. Expliquer ce qui mérite d'être repris, adapté ou écarté. Une solution populaire ou récente doit encore convenir au produit. L'innovation peut résider dans une composition ou un parcours original fondé sur des composants éprouvés.

Citer les pages précises près des décisions qu'elles soutiennent. Vérifier le statut d'un standard avant de le traiter comme référence de conformité ; un brouillon ne remplace pas automatiquement une recommandation publiée. Cette recherche a lieu pendant la mission ; ne pas promettre une veille permanente ou créer une automatisation sans demande.

Si la recherche est indisponible, signaler la limite et poursuivre avec les éléments accessibles. Ne pas inventer de benchmark, de disponibilité technique, d'étude ou de métrique.

## Construire et choisir la solution

- Relier **observation ou hypothèse → effet utilisateur → proposition concrète → vérification**. Donner un libellé, une disposition, une interaction ou un état précis.
- Pour une création ou une refonte substantielle, explorer des directions visuelles distinctes selon le guide artistique, sauf si une direction ou un système existant répond déjà à la demande. Montrer les alternatives sur un même écran représentatif avec les mêmes contenus. Proportionner le nombre et le niveau de finition au vrai arbitrage ; une retouche locale ne nécessite pas trois maquettes.
- Recommander une direction avec son compromis principal. Quand une sélection utilisateur est nécessaire, avancer sur le parcours et les travaux communs en attendant ; ne pas engager l'implémentation coûteuse d'une direction encore indécise.
- Décliner la direction retenue en règles et composants réutilisables : rôles des couleurs, typographie, espacements, densité, iconographie, mouvement et états. Partager l'identité et les concepts métier entre plateformes tout en adaptant navigation, commandes et comportements.
- Montrer les choix spatiaux par un wireframe, une maquette ou un prototype quand cela aide à décider. Préciser si le résultat est une exploration graphique, un prototype ou une interface fonctionnelle. Utiliser les outils disponibles sans supposer un service ou un abonnement particulier.
- Prioriser selon la gravité pour la tâche, l'étendue connue, l'effort et les dépendances. Distinguer corrections nécessaires, améliorations plausibles et explorations. Qualifier les estimations ; ne pas fabriquer de scores de qualité ou de fréquence.

## Implémenter et vérifier lorsque demandé

Réutiliser les composants, conventions et technologies du projet. Ne pas imposer un framework, un fournisseur ou une refonte technique pour obtenir un style. Justifier une dépendance par le besoin et son coût de maintenance. Traiter les états et adaptations qui conditionnent réellement le parcours.

Appliquer les contrôles pertinents du guide de vérification, puis examiner le rendu réel. Corriger les défauts observés et revérifier les zones touchées jusqu'à résolution du périmètre accessible ou identification précise d'une limite. Une maquette ou une compilation réussie ne suffit pas à valider une interaction. Pour une livraison couvrant plusieurs plateformes, préciser celles effectivement vérifiées.

Distinguer contrôles automatiques, vérifications manuelles et tests réalisés avec des utilisateurs. Un outil d'accessibilité ne démontre pas une conformité globale. Pour une création, formuler les gains attendus comme hypothèses ; annoncer un gain mesuré seulement avec des données comparables.

## Livrer un résultat exploitable

Commencer par la recommandation ou le résultat. Adapter le livrable à la mission :

- **Audit** : écran ou étape, preuve, effet utilisateur, correction, priorité, effort estimé et validation ; distinguer défaut observé et difficulté à tester.
- **Conception** : parcours, direction recommandée et visuel pertinent, comportements et états essentiels, règles de composants, adaptations par plateforme, sources et hypothèses restantes.
- **Implémentation** : changements réalisés, rendu ou captures utiles, parcours et environnements vérifiés, limites concrètes et prochaines vérifications nécessaires.

Ne pas imposer un dossier complet à chaque demande. Conserver les livrables et la documentation dans les formats et emplacements convenus pour le projet.
