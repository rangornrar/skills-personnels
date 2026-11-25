# Maquettes, code et vérification

Lire pour concevoir les écrans, implémenter une tranche fonctionnelle ou vérifier les parcours.

## Produire une maquette qui permet de décider

Définir le point d'entrée du scénario, ses étapes, son résultat et les possibilités de retour, d'annulation ou de reprise. Décrire les transitions lorsque le support ne permet pas de les exécuter.

Commencer au niveau de fidélité qui résout l'incertitude : wireframe pour la structure, maquette visuelle pour la présentation, prototype navigable pour les interactions. Ne pas imposer trois productions successives si une seule suffit.

Utiliser des contenus proches de l'usage et les états qui changent le parcours : vide, chargé, attente, succès, erreur, saisie invalide, permission refusée et réseau absent selon le besoin. Les données fictives doivent être identifiées et sans données personnelles réelles.

Sur mobile, examiner navigation, retour, clavier virtuel, rotation ou adaptation si pertinent, zones système et permissions. Sur bureau, examiner redimensionnement, clavier, focus, fenêtres et actions fréquentes. Sur web, examiner tailles utiles, navigation, clavier et comportements navigateur.

S'appuyer sur le système de composants existant et les conventions actuelles de la plateforme. Prévoir lisibilité, ordre du focus, noms accessibles, contrastes et agrandissement. Vérifier les référentiels applicables avant d'annoncer des seuils ou une conformité.

Donner un accès au rendu : fichier, outil de conception disponible, captures ou prototype exécutable. Si un prototype web représente une future app native, préciser cette portée et les interactions natives encore simulées. Une image générée ne constitue ni du code ni une preuve de faisabilité.

Une préférence visuelle non tranchée permet généralement de poursuivre le socle. Un désaccord qui change le parcours, les données ou le périmètre mérite un arbitrage ciblé, avec une proposition concrète à examiner.

## Réaliser par parcours utilisables

Avant une modification, examiner les conventions, la configuration de build, les dépendances, les tests existants et les changements locaux. Préserver le travail de l'utilisateur.

Créer une première tranche verticale : une tâche utilisateur utile fonctionne de son entrée à son résultat, avec la persistance ou l'intégration requise. Ne pas remplir tous les écrans de boutons sans comportement et présenter ce squelette comme un produit terminé.

Choisir les itérations suivantes selon valeur, dépendances et risque. Pour chacune :
1. Retenir le scénario et les critères de réussite.
2. Implémenter le comportement, les états d'erreur et la récupération nécessaires.
3. Exécuter les contrôles pertinents et corriger les défauts constatés.
4. Actualiser les documents et l'état de reprise affectés.

Les mocks servent à isoler un composant ou explorer une interface. Identifier les simulations et raccorder les services réels nécessaires avant de déclarer le scénario complet. Ne pas masquer l'absence d'un backend, d'un paiement ou d'une API système derrière un écran de succès fictif.

Traiter sécurité et confidentialité en fonction des données et des points d'entrée réels : validation des entrées, autorisation côté service, stockage approprié, protection des secrets et minimisation des données. Ne pas imposer un système de comptes à une application qui n'en a pas besoin.

Pour une installation ou modification d'outillage coûteuse ou persistante hors projet, évaluer le besoin et utiliser les autorisations disponibles ; une simple préférence de stack ne justifie pas de reconfigurer toute la machine.

## Vérifier ce qui compte pour la livraison

Adapter les contrôles au comportement :
- Build, analyse statique et vérifications déjà requises par le projet.
- Tests de logique pour les règles et cas limites matériels.
- Tests d'intégration pour les données, API, migrations et permissions affectées.
- Recette du scénario principal, de ses erreurs importantes et de la conservation des données attendue.
- Inspection du rendu aux tailles et états pertinents ; contrôles clavier, focus et accessibilité applicables.
- Essais sur émulateur, simulateur ou appareil lorsque disponibles, en précisant lesquels.
- Installation et lancement du paquet de livraison lors de sa préparation.

Éviter les tests qui répètent l'implémentation sans vérifier un résultat observable. Après réussite des contrôles appropriés, ne pas relancer une suite complète sans nouvelle raison.

Relier chaque résultat aux critères prioritaires. Conserver commande ou scénario, environnement, version et résultat. « Non exécuté » doit rester distinct de « réussi » ; indiquer un accès ou un outil manquant plutôt que fabriquer une vérification.

Une compilation ne prouve pas le fonctionnement du parcours ; un test sur émulateur ne prouve pas toutes les caractéristiques d'un appareil physique. Qualifier précisément la preuve, puis proposer la vérification complémentaire seulement si elle est utile à la cible.
