# Vérifier l'expérience et le rendu

Lire pour un audit, un prototype interactif ou une implémentation. Sélectionner les vérifications selon la tâche et les surfaces modifiées ; un défaut local ne justifie pas une campagne complète. Définir les preuves attendues avant d'annoncer un résultat.

## Choisir des conditions représentatives

Pour un changement substantiel, relever les parcours critiques, états et tailles de fenêtre concernés. Utiliser les versions, appareils, navigateurs et entrées du périmètre ; identifier les environnements accessibles et ceux qui restent à vérifier. Une vérification web sur ordinateur ne valide pas une application native iOS ou Android.

Choisir des données qui révèlent les risques du parcours : absence de résultats, noms longs, traductions, valeurs limites ou volumes élevés si pertinents. Pour la création, expliciter ces hypothèses ; pour un produit existant, partir des contenus disponibles.

## Examiner les dimensions touchées

| Dimension | Contrôles possibles | Preuve utile |
| --- | --- | --- |
| Parcours | Comprendre le point de départ, retrouver l'action, accomplir la tâche, revenir ou annuler | Étapes parcourues, état final, difficulté localisée |
| Robustesse | Attente, erreurs et reprise ; saisie conservée ; absence de double action involontaire | Scénario et comportement observés |
| Présentation | Hiérarchie, densité, alignements, textes, composants et états cohérents | Rendu à taille réelle, capture annotée si utile |
| Adaptation | Redimensionnement, orientation, zoom ou échelle, clavier logiciel, contenus longs | Conditions testées et débordement ou perte d'action identifiés |
| Accessibilité | Clavier, focus, noms et états accessibles, contrastes, agrandissement et préférences système | Mesure ou interaction précise, critère applicable et résultat |
| Performance perçue | Retour immédiat à l'action, stabilité de l'affichage, réactivité sur le parcours | Observation ou mesure avec environnement et conditions |

Pour l'accessibilité, consulter les critères détaillés et exceptions du [référentiel WCAG retenu](https://www.w3.org/WAI/WCAG22/quickref/) et les recommandations natives du guide des plateformes. Vérifier les contrastes avec les couleurs réellement affichées, y compris sur fond variable. Vérifier les dimensions des cibles dans les unités de la plateforme ; ne pas déclarer un seuil universel en « pixels ».

Pour les composants concernés, examiner l'ordre du focus, son retour après fermeture d'une fenêtre modale, les erreurs de formulaire et les changements d'état. Vérifier séparément les annonces avec un lecteur d'écran disponible : une capture ou un attribut dans le code ne prouve pas une restitution correcte. Exercer les préférences de mouvement réduit, d'agrandissement ou de contraste lorsqu'elles affectent la solution.

## Utiliser les outils comme preuves partielles

- Exécuter les contrôles du projet adaptés à la modification. Utiliser les outils automatiques pertinents disponibles pour détecter les problèmes qu'ils savent identifier ; vérifier manuellement navigation, compréhension et interactions affectées.
- Tester les composants modifiés avec leurs comportements attendus lorsque le risque le justifie. Éviter les tests qui vérifient seulement la présence du style ou reproduisent la structure du code.
- Pour un audit, rattacher chaque constat à une étape, un écran ou un élément identifiable. Séparer défaut observé, difficulté probable à tester et préférence artistique.
- Pour une maquette fixe, vérifier la composition et les états représentés ; identifier les comportements encore non démontrés. Pour un prototype, indiquer les limites de simulation, de données et d'intégration.

## Itérer sur le produit réel

Après modification, examiner le rendu et exécuter la tâche. Corriger les défauts observés, puis revérifier les zones affectées. Comparer avant et après dans des conditions équivalentes lorsque cette comparaison éclaire le résultat. Refaire ou élargir les contrôles si une modification, une régression ou une incertitude concrète le justifie.

Une itération est terminée lorsque les problèmes du périmètre accessible sont résolus et que les limites restantes sont explicitement identifiées. Distinguer un blocage empêchant la tâche d'une amélioration supplémentaire ; ne pas élargir indéfiniment la mission.

## Tester avec des utilisateurs lorsque pertinent

Proposer une tâche réaliste et un public concerné, avec des critères d'observation : réussite sans aide, erreurs, hésitations, compréhension et reprise. Formuler la consigne sans révéler la solution. Adapter le protocole aux moyens et au risque ; une exploration qualitative ne permet pas de quantifier un gain de population.

Ne pas présenter l'auto-évaluation, un outil automatique ou une simulation par IA comme un test avec des utilisateurs. Comparer temps ou taux de réussite seulement avec des conditions et données suffisamment comparables. Une expérimentation A/B demande un trafic et un protocole adaptés.

## Rapporter ce qui est établi

Pour une restitution importante, donner **contrôle ou parcours | environnement et conditions | résultat et preuve | reste à vérifier**, en séparant automatique, manuel et utilisateurs. Pour une petite modification, quelques phrases peuvent suffire.

Décrire les défauts avec leur conséquence et leur correction. Nommer les limites concrètes : par exemple « retour système vérifié sur émulateur Android ; validation sur appareil et TalkBack non réalisée ». Ne pas annoncer une certification, une conformité globale ou un gain UX mesuré sur la base de contrôles partiels.
