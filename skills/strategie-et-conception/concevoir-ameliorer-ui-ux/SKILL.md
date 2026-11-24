---
name: concevoir-ameliorer-ui-ux
description: "Concevoir ou améliorer l'UI et l'UX d'un logiciel de bureau, web ou mobile à partir des usages, de l'interface et de recherches externes ciblées. Utiliser pour un audit ergonomique, une création d'interface, une refonte, un benchmark de produits comparables ou des propositions UI/UX argumentées et priorisées ; accompagner l'implémentation lorsqu'elle est demandée. Ne pas déclencher pour une correction technique sans enjeu d'interface ni pour un simple visuel marketing."
---

# Concevoir et améliorer une interface utile

Répondre en français sauf demande contraire. Relier les choix d'interface aux tâches des utilisateurs, aux conventions de la plateforme et aux contraintes du produit. Produire des solutions concrètes, appuyées sur des observations et une recherche ciblée. Adapter la profondeur au périmètre : une correction locale ne nécessite pas une refonte complète.

## Cadrer le travail

- Déterminer s'il faut créer, diagnostiquer, comparer des solutions ou implémenter. Une demande de propositions conduit à des propositions ; une demande de modification inclut la réalisation et la vérification dans le périmètre autorisé.
- Identifier les utilisateurs, leurs tâches principales, leur niveau d'expertise, la plateforme, les modes d'entrée et les contraintes connues : identité visuelle, composants existants, stack, budget ou délai. Déduire ce qui peut l'être du projet et signaler les hypothèses qui influencent les choix.
- Consulter les consignes du projet et le système de design existant avant de proposer un remplacement. Ce skill est transversal et ne suppose aucun framework, fournisseur ou projet particulier.
- Poser une à trois questions ciblées seulement si une réponse peut modifier sensiblement le travail. Continuer les recherches et observations indépendantes de ces réponses.
- Retenir un critère de réussite observable : accomplir une tâche sans aide, retrouver une commande, corriger une erreur, accéder au parcours au clavier. Sans mesure initiale, proposer une façon de l'établir plutôt qu'un gain chiffré inventé.

## Observer ou construire le parcours

### Programme existant

- Examiner l'application réelle lorsqu'elle est accessible. Capturer les écrans et parcourir les interactions pertinentes avant de conclure sur leur apparence ou leur comportement. Utiliser les outils d'inspection ou de contrôle disponibles selon leurs règles ; le code complète l'observation du rendu.
- Travailler à partir des captures, spécifications et fichiers disponibles si l'exécution est impossible. Préciser la limite : une capture permet d'examiner la hiérarchie visuelle, mais ne démontre ni le fonctionnement du clavier ni celui des annonces d'un lecteur d'écran.
- Suivre la tâche de son point d'entrée à son résultat, en incluant les états utiles : premier usage, données présentes ou absentes, attente, succès, erreur, annulation et reprise. Ne pas créer un inventaire exhaustif si le besoin porte sur un seul écran.
- Rattacher chaque constat à un écran, un composant, une étape ou un extrait identifiable. Distinguer un défaut observé, une difficulté probable à tester et une préférence esthétique.

### Nouvelle interface

- Définir le scénario principal, les informations nécessaires et les actions avant le style graphique. Ébaucher le parcours et la structure des écrans à partir de contenus représentatifs.
- Prévoir les états et les contraintes de fenêtre ou d'appareil qui affectent ce scénario. Décrire les hypothèses de conception comme telles, sans les présenter comme des problèmes observés ou des besoins validés.

## Chercher ce qui se fait et en tirer des décisions

- Effectuer une recherche externe ciblée pour une conception, un audit ou une amélioration substantielle, ainsi que lorsque l'utilisateur demande des références ou tendances. Réutiliser des sources déjà vérifiées dans la session si elles restent pertinentes. Pour une correction ponctuelle établie, ne pas imposer un benchmark complet.
- Formuler la recherche autour du problème et du contexte : par exemple, validation de formulaires sur mobile, configuration dans une application de bureau ou navigation dans un outil métier dense. Une recherche de « belles interfaces modernes » ne suffit pas.
- Chercher deux types d'éléments lorsque cela apporte une réponse : recommandations officielles de la plateforme ou standards applicables, et exemples actuels de produits accomplissant une tâche comparable. Quelques références bien choisies valent mieux qu'une longue galerie.
- Ouvrir les sources utiles ; vérifier leur contenu, leur contexte et leur actualité. Pour les produits comparés, distinguer un parcours testé, une démonstration officielle, une capture marketing et une simple description. Ne pas prétendre avoir utilisé un produit sur cette seule base.
- Pour chaque référence retenue, expliquer le mécanisme intéressant, le problème qu'il pourrait résoudre ici et la limite de sa transposition. Comparer les utilisateurs, la densité d'information et les modes d'entrée ; ne pas importer automatiquement un modèle mobile dans un outil de bureau.
- Citer les pages précises près des propositions qu'elles étayent. Donner une date ou version lorsqu'elle influe sur le choix. Un exemple populaire illustre une solution ; il ne prouve pas son efficacité. Une tendance visuelle reste une préférence tant que son bénéfice n'est pas étayé.
- Si la recherche est indisponible, annoncer la limite et poursuivre avec les éléments accessibles. Ne pas inventer de benchmark, d'étude, de métrique ou de test utilisateur.

Points d'entrée officiels à sélectionner selon le contexte, puis approfondir vers les pages pertinentes ; vérifier les versions applicables au moment de l'usage :

| Contexte | Point d'entrée |
| --- | --- |
| Accessibilité web | [W3C — référence WCAG](https://www.w3.org/WAI/WCAG22/quickref/) |
| Applications Windows | [Microsoft — recommandations de conception](https://learn.microsoft.com/en-us/windows/apps/design/guidelines-overview) |
| Plateformes Apple | [Apple — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) |
| Écosystème Material | [Material — fondations](https://m3.material.io/foundations/) |

Ces sources sont des points de départ, pas un style imposé. Pour le web, utiliser les critères WCAG de niveau AA comme cible de conception par défaut si aucun référentiel n'est fourni ; vérifier leur version et leur périmètre. Pour le natif, compléter avec les recommandations et API d'accessibilité de la plateforme. Ne pas annoncer une conformité globale à partir d'un contrôle partiel.

## Examiner les dimensions qui affectent la tâche

Sélectionner les angles utiles, sans produire une liste de contrôle indifférenciée :

- **Parcours et information :** repérage, regroupement, vocabulaire, navigation, nombre d'étapes utiles, retour en arrière, équilibre entre débutants et utilisateurs experts.
- **Interaction :** actions identifiables, retour d'état, prévention et récupération des erreurs, saisie, confirmation ou annulation proportionnée, raccourcis et actions fréquentes.
- **Présentation :** hiérarchie, lisibilité, densité, alignements, espacements, cohérence des composants, couleur et iconographie au service de la compréhension. Préserver une identité adaptée au produit ; éviter une recette visuelle systématique.
- **Accessibilité et adaptation :** clavier, focus visible et logique, noms et états accessibles, contrastes mesurés, sens communiqué au-delà de la couleur, taille des cibles, zoom ou mise à l'échelle, redimensionnement et réduction des animations. Vérifier les seuils dans le référentiel applicable plutôt que mélanger pixels CSS, points et unités natives.
- **Contenu et robustesse :** libellés précis, aide contextuelle, textes longs ou traduits, grands volumes, états vides et dégradés, attente et maintien du travail déjà saisi.

Ne pas confondre simplicité et suppression de fonctions utiles. Pour un outil expert, une interface dense, des raccourcis ou des actions groupées peuvent mieux servir la tâche qu'un parcours dispersé. Éviter les interactions trompeuses, les coûts cachés et les choix difficiles à annuler pour augmenter artificiellement une conversion.

## Proposer, comparer et prioriser

- Pour une amélioration substantielle, relier **observation ou hypothèse → conséquence utilisateur → solution précise → vérification**. Donner un libellé de remplacement, une disposition, une règle d'interaction ou un état concret, plutôt que « améliorer l'ergonomie ».
- Séparer les corrections nécessaires, les améliorations plausibles et les explorations visuelles. Prioriser selon la gravité pour la tâche, la fréquence ou l'étendue connue, l'effort et les dépendances. Qualifier l'effort comme estimation si le code n'a pas été examiné ; ne pas fabriquer de scores ou de fréquences.
- Comparer plusieurs directions seulement si un vrai arbitrage le justifie. Inclure une évolution limitée de l'existant lorsqu'elle est viable, puis recommander une option avec son compromis et la condition qui ferait changer d'avis.
- Examiner l'objection principale : coût d'apprentissage, perte de densité, fonction moins accessible, dépendance supplémentaire ou coût de réalisation. Ne pas confondre réduction du nombre de clics et amélioration du parcours.
- Rendre visible une proposition spatiale quand cela facilite la décision : schéma, wireframe, maquette ou prototype adapté aux outils disponibles. Un visuel fixe illustre une apparence ; vérifier séparément les interactions.

## Réaliser et vérifier lorsque demandé

- Réutiliser les composants et styles du projet. Introduire une nouvelle dépendance ou une refonte du système de design seulement si le besoin le justifie ; expliquer le coût et le bénéfice.
- Implémenter les états qui conditionnent le parcours, au-delà du seul écran idéal. Conserver les fonctions utiles et traiter les adaptations pertinentes à la plateforme.
- Exécuter les contrôles du projet appropriés et vérifier le rendu réel après modification, aux tailles et états concernés. Parcourir la tâche principale, le clavier et les erreurs affectées ; comparer les captures avant et après lorsque cela éclaire le résultat.
- Distinguer ce qui a été vérifié automatiquement, manuellement, et ce qui reste à tester avec des utilisateurs. Ne pas qualifier une auto-évaluation de test utilisateur ni présenter une intention de conception comme un gain mesuré.
- Si un test utilisateur est pertinent, proposer une tâche réaliste sans indiquer la solution, un public concerné et des observations utiles : réussite, erreurs, hésitations, temps et compréhension. Ne pas imposer un test statistique ou une expérimentation A/B sans trafic et conditions adaptés.

## Restituer un résultat exploitable

Commencer par la recommandation utile et les changements prioritaires. Adapter le format au besoin ; un audit complet peut utiliser un tableau **écran ou étape | preuve | effet utilisateur | proposition | priorité et effort | validation**, suivi des références et du compromis principal. Garder les sources près des affirmations concernées.

Pour une création, livrer le parcours proposé, les écrans et comportements essentiels, la direction visuelle et les hypothèses à valider. Pour une implémentation, indiquer ce qui a changé, les vérifications réalisées et les limites restantes. Un besoin local peut se satisfaire d'une réponse courte ; ne pas imposer toutes les rubriques à chaque utilisation.
