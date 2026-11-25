# Corrections, spécifications et documentation

## Préserver le besoin et l'état initial

Archiver ou référencer la version des spécifications d'origine, les décisions et l'état du code audité. Dans un dépôt modifié localement, le commit seul ne décrit pas tout l'état : relever aussi les changements utiles sans publier leur contenu sensible.

Pour chaque exigence existante, conserver son identifiant et sa source. Classer l'état observé : satisfait avec preuve, partiel, absent, défectueux, ambigu, non vérifié ou hors périmètre confirmé. Si les spécifications sont introuvables, reconstruire une description de l'existant explicitement intitulée **spécifications reconstituées**, à confirmer ; elle ne représente pas les intentions historiques.

Un écart peut être un défaut ou une évolution acceptée. Rechercher la décision correspondante. Sans décision, consigner l'écart et proposer un arbitrage. Préserver les exigences proposées comme propositions ; une implémentation ne vaut pas acceptation d'un nouveau besoin.

## Réaliser les changements utiles

Associer chaque lot à ses constats, au comportement cible, aux fichiers concernés, aux dépendances et aux vérifications pertinentes. Commencer par les blocages et dépendances ; limiter la refonte à ce que justifient l'objectif et les preuves. Préserver les données et les modifications de l'utilisateur.

Pour une modification risquant de changer le contrat utilisateur, les données persistées, la plateforme ou les coûts, préparer l'impact et une solution concrète avant l'arbitrage éventuellement nécessaire. Réutiliser l'autorisation existante si elle couvre déjà le changement.

Pour une correction fonctionnelle ou un risque significatif, tester le comportement nominal, l'erreur pertinente et la régression ciblée. Ne pas ajouter des tests qui reproduisent simplement l'implémentation ou prétendent valider une interface en ne vérifiant que son texte. Utiliser les commandes du projet et consigner résultat, environnement et version. Séparer tests automatiques, essais manuels et contrôles empêchés.

Si un contrôle échoue, conserver la preuve, corriger si possible, puis relancer les contrôles affectés. Ne pas multiplier les essais coûteux identiques sans information nouvelle. Un correctif seulement relu reste « réalisé, non vérifié » ; un échec d'infrastructure n'est ni une réussite ni automatiquement un défaut du produit.

## Mettre à jour les documents concernés

| Document | Mise à jour attendue |
| --- | --- |
| README d'entrée | Utilité, démarrage réel, démonstration ou capture si disponible, limites, liens utiles |
| Guide utilisateur | Parcours principaux, entrées/sorties, erreurs fréquentes et récupération |
| Spécifications actualisées | Origine conservée, décisions intégrées, changements proposés séparés, critères d'acceptation |
| Architecture | Contexte, composants réels, responsabilités, données et flux, intégrations, configuration, déploiement et compromis |
| Tests | Commandes, prérequis, périmètre des suites, mesures réellement produites et lacunes restantes |
| Installation et mises à jour | Cibles, versions requises, droits, configuration, première exécution, migration et désinstallation |
| Exploitation | Déploiement, logs, sauvegarde/restauration, retour arrière, diagnostic et support selon usage |
| Notes de changement | Problème, nouveau comportement, migration ou incompatibilité et vérifications importantes |

Adapter ce découpage à la taille du projet : quelques sections peuvent suffire. Ne pas créer une collection de documents vides. Décrire ce qui existe et distinguer les architectures ou procédures cibles proposées. Mettre un sommaire dans les guides substantiels ; placer utilité, usage et sorties avant installation, architecture et détails techniques.

## Fermer un constat avec une preuve

Conserver la gravité initiale et les preuves d'origine. Ajouter changement, vérification, résultat et risque résiduel. Statuts conseillés : ouvert, en cours, réalisé non vérifié, vérifié, bloqué, différé, risque accepté. « Risque accepté » requiert une décision identifiable de l'utilisateur ; un report de l'agent ne suffit pas.

Actualiser le PDF et le plan d'actions après les corrections. Les livrables finaux décrivent la version après changements ; le diagnostic initial reste consultable. Ne pas laisser la synthèse recommander une correction déjà terminée ni présenter comme effectué un déploiement simplement préparé.
