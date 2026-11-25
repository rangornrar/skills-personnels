# Adapter la conception à la plateforme

Lire les sections correspondant aux cibles et aux décisions de la mission. Les sources ci-dessous sont des points d'entrée officiels, pas des versions figées ni des styles imposés. Vérifier au moment du travail les recommandations détaillées, versions minimales et composants réellement disponibles dans la stack. Un framework multiplateforme ne dispense pas des adaptations.

## Principes communs aux produits multiplateformes

Partager les concepts métier, le vocabulaire et une identité reconnaissable. Définir par plateforme ce qui doit varier : navigation, placement des commandes, densité, raccourcis, menus, retours d'état et interactions système. Choisir selon l'espace disponible et les entrées actives ; ne pas déduire le comportement de la seule étiquette « mobile » ou « bureau ».

Pour le natif, compléter les recommandations de plateforme par [WCAG2ICT](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/) lorsque pertinent. Il s'agit d'un guide d'application des principes WCAG aux technologies non web, à distinguer d'une certification du produit. Ne pas transposer mécaniquement les unités CSS aux points Apple ou aux unités Android et Windows.

## Windows

Point d'entrée : [Microsoft — Design Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/). Chercher les recommandations de navigation, commandes, mise en page, accessibilité et matériaux utiles au cas traité.

- Concevoir pour souris, clavier et, lorsque pertinent, tactile. Prévoir un focus logique et visible, les raccourcis utiles, les menus contextuels et une alternative accessible aux interactions de précision.
- Adapter navigation et panneaux au redimensionnement réel de la fenêtre. Pour un outil expert, préserver recherche, tri, sélection multiple, actions groupées et densité utile lorsqu'ils répondent aux tâches.
- Préserver les interactions de la fenêtre : déplacement, redimensionnement, commandes système et zones interactives de la barre de titre si elle est personnalisée. Vérifier la mise à l'échelle et les réglages d'accessibilité concernés, dont les thèmes de contraste.
- Réutiliser les composants et sémantiques accessibles de la stack. Pour des composants personnalisés, vérifier leur exposition aux technologies d'assistance Windows ; tester avec Narrator lorsque disponible et pertinent.
- Évaluer les matériaux Fluent selon la version, le framework et les préférences système. Prévoir une surface lisible sans effet ; ne pas imposer une migration technique pour reproduire un matériau.

## Android

Points d'entrée : [Android — Material 3 dans Compose](https://developer.android.com/develop/ui/compose/designsystems/material3) et [Android — Adaptive Apps](https://developer.android.com/develop/adaptive-apps). La documentation Material présente aussi les évolutions Expressive ; vérifier séparément le statut des composants concernés.

- Adapter navigation et disposition à la fenêtre : téléphone, tablette, pliable ou mode fenêtré selon le périmètre. Évaluer liste-détail, panneaux d'appui et navigation adaptée à l'espace disponible plutôt qu'agrandir uniformément un écran de téléphone.
- Préserver sélection, saisie et étape du parcours lors des changements de taille ou d'orientation. Traiter le retour système et vérifier le retour prédictif lorsqu'il fait partie des versions et composants ciblés.
- Tenir compte des barres système, découpes, gestes de navigation et clavier logiciel. Éviter qu'une action ou une erreur soit masquée par ces éléments.
- Prévoir cibles tactiles, agrandissement de texte et sémantique pour TalkBack. Ajouter clavier, souris ou stylet si les usages et appareils cibles le nécessitent ; ne pas rendre une action essentielle dépendante du seul survol.
- Employer les composants du projet ; comparer les possibilités Material, dont Expressive ou la couleur dynamique, à l'identité et aux préférences attendues. Ne pas traiter tous leurs éléments comme interchangeables ni disponibles dans toute version de bibliothèque.

## iOS et iPadOS ; autres plateformes Apple selon le besoin

Point d'entrée : [Apple — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/). Pour les matériaux récents : [Apple — Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/liquid-glass). Si une page nécessite JavaScript, utiliser sa version Markdown officielle lorsqu'elle est proposée.

- Respecter les conventions de navigation, retour, présentation modale et commandes de la plateforme ciblée ; maintenir une sortie compréhensible et la continuité du parcours. Éviter qu'un geste caché soit l'unique accès à une fonction essentielle.
- Sur iPhone, vérifier la portée tactile et l'occupation par le clavier. Sur iPad, adapter panneaux, multitâche et commandes aux fenêtres et modes d'entrée réellement ciblés ; conserver le contexte lors du redimensionnement.
- Prévoir zones de sécurité, agrandissement typographique avec Dynamic Type, sémantique VoiceOver et réglages système pertinents. Tenir compte de la réduction du mouvement et de la transparence pour les traitements concernés.
- Favoriser les composants natifs ou les équivalents accessibles de la stack. Évaluer Liquid Glass sur les systèmes compatibles et dans les emplacements recommandés ; vérifier lisibilité et comportement sur différents fonds. Prévoir un traitement compatible avec les versions antérieures retenues.
- Pour macOS ou une autre cible Apple, rechercher ses conventions propres avant de décliner une interface iOS. Conserver l'identité sans supposer les mêmes commandes, entrées ou contraintes de fenêtre.

## Web : sites, applications et PWA

Points d'entrée : [W3C — WCAG 2.2, référence rapide](https://www.w3.org/WAI/WCAG22/quickref/), [W3C — ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/), et [MDN — compatibilité des technologies web](https://developer.mozilla.org/en-US/docs/Web). Pour une capacité précise, ouvrir sa documentation et ses données de compatibilité.

- Utiliser par défaut WCAG 2.2 niveau AA comme cible de conception, sous réserve du référentiel fourni et de son périmètre ; vérifier l'actualité de la référence. Distinguer la cible choisie de la conformité effectivement évaluée et des obligations applicables au projet.
- Préférer les éléments HTML sémantiques et contrôles natifs appropriés. Pour les widgets personnalisés, consulter le pattern concerné et vérifier rôles, noms, états et interactions clavier ; ajouter de l'ARIA ne remplace pas le comportement.
- Préserver l'usage du navigateur : liens, historique, retour, accès direct et partage d'une URL lorsque pertinent. Traiter le focus et les annonces lors des changements de vue, ainsi que le clavier, le zoom et l'agrandissement des textes.
- Concevoir des adaptations à partir du contenu et de la fenêtre, avec les entrées tactiles et de pointage concernées. Vérifier les zones fixes, fenêtres modales, claviers logiciels, tableaux larges et contenus longs dans les conditions utiles au produit.
- Évaluer les possibilités actuelles telles que requêtes de conteneur, transitions de vue, popovers ou nouveaux contrôles en fonction des navigateurs ciblés et de l'accessibilité. Vérifier disponibilité et compatibilité avant de choisir ; conserver un parcours utilisable lorsque l'amélioration est absente.
- Pour une PWA, traiter installation, mode hors ligne et permissions seulement s'ils font partie des besoins. Pour les performances, mesurer le parcours et les appareils pertinents ; éviter les effets qui gênent réactivité ou stabilité de l'affichage.
