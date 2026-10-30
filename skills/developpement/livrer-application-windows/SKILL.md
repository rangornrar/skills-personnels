---
name: livrer-application-windows
description: "Préparer et vérifier la livraison d'une application Windows depuis son dépôt : modifications, tests, compilation, versions, notes, paquets et release GitHub. Utiliser pour livrer SnapSlate, Transcript ou une application comparable ; ne pas déclencher pour un simple cadrage ou un dépannage Windows sans code applicatif."
---

# Préparer une livraison Windows vérifiable

Lire les consignes du dépôt, la documentation de build, les workflows et l'état Git avant de modifier. Identifier le commit visé, la branche, la stack réelle, les cibles Windows et le mode de distribution. Ne pas supposer qu'une application MSIX utilise WinUI ni réutiliser les commandes d'un autre projet.

## Définir la livraison

Relier les changements à un problème et à un comportement observable. Préserver le travail local existant ; isoler les modifications lorsqu'il le faut. Identifier les assets, modèles, configurations et données qui doivent ou ne doivent pas entrer dans le paquet.

Séparer une correction locale, un build prêt à examiner, une release publiée et une soumission à un store. Une demande de préparation n'autorise pas toutes les étapes externes. Une autorisation déjà donnée reste valable dans son périmètre.

## Réaliser et vérifier

- Utiliser les scripts et dépendances du projet, vérifier les versions dans leurs fichiers de référence et la documentation officielle lorsqu'une compatibilité est en jeu.
- Tester le comportement modifié, les erreurs pertinentes et le parcours principal. Une compilation réussie ne prouve pas le bon fonctionnement de l'interface.
- Exécuter les contrôles requis, puis le build avec la configuration de livraison. Ne pas relancer toute la suite sans changement ou doute nouveau.
- Vérifier les chemins, encodages, droits nécessaires et ressources embarquées. Pour les modèles ou binaires externes, contrôler les licences et la stratégie de distribution réellement retenue.
- En cas de test impossible, nommer le contrôle non réalisé et son implication. Ne pas annoncer « tout au vert » sur la base d'une partie des checks.

## Versionner et empaqueter

Suivre le schéma de version du projet, vérifier cohérence entre application, manifeste, artefact et tag. Générer le paquet attendu et contrôler architecture, contenu, taille et métadonnées utiles. Ne pas créer de certificat, modifier une politique de signature ou réduire une protection pour contourner un blocage.

Rédiger les notes autour du problème corrigé et du résultat utilisateur, avec les limites matérielles. Identifier le commit et calculer l'empreinte des livrables utiles. Distinguer tests automatisés, essais manuels et contrôles encore attendus sur une machine cible.

## Publier lorsque demandé

Utiliser les outils GitHub disponibles et les autorisations existantes. Vérifier les fichiers et le commit attachés avant publication. Pour un échec de CI, lire les logs correspondant au bon commit avant de corriger ; un statut d'un ancien commit ne valide pas le nouveau.

Pour un store, vérifier ses exigences actuelles et le périmètre autorisé. Fournir le lien de release ou le chemin du paquet effectivement créé ; ne pas annoncer une soumission ou une approbation non constatée. Documenter la manière de revenir à la version précédente si la livraison l'exige.
