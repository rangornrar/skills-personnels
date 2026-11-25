---
name: auditer-ameliorer-produit
description: "Auditer un logiciel existant de bout en bout, confronter son fonctionnement aux besoins initiaux, puis réaliser les corrections et mises à jour documentaires demandées. Produire un rapport PDF sourcé et un plan de suite couvrant qualité produit, technique, exploitation, visibilité et commercialisation. Utiliser pour une revue globale ou une remise à niveau d'un outil ; ne pas déclencher pour un bug isolé, une simple revue de code ou le cadrage d'une idée sans produit existant."
---

# Auditer et améliorer un produit existant

Répondre en français sauf demande contraire. Examiner le produit réellement disponible, ses usages et ses contraintes. Le résultat doit permettre de décider quoi conserver, corriger, abandonner, vérifier ou lancer ensuite, et de retrouver les preuves de chaque conclusion.

## Cadrer sans recommencer le projet

Lire les consignes locales, l'état du dépôt, les spécifications et décisions existantes avant toute modification. Identifier version ou commit, éventuelles modifications locales, plateforme, utilisateurs, parcours essentiels, accès disponibles et objectif : usage personnel, partage, diffusion gratuite ou vente. Ne pas déduire que le produit à auditer est celui d'une ancienne conversation sans référence suffisamment claire.

Retenir le périmètre donné par l'utilisateur. S'il manque le produit ou son accès, demander le dépôt, dossier, URL ou fichiers disponibles ; préparer entre-temps la grille et les livrables, sans fabriquer de constats. Poser au plus trois questions matérielles par lot ; ne pas redemander les informations présentes dans les sources accessibles.

Adapter l'exécution à la demande :

- **Audit** : examiner et produire le dossier ; ne pas modifier l'application ou ses documents existants sous prétexte qu'une correction serait utile.
- **Audit et mise à niveau** : réaliser aussi les corrections locales et mises à jour documentaires demandées, puis vérifier et actualiser le dossier. Une demande générale d'amélioration autorise les correctifs cohérents avec le besoin établi, pas une refonte du produit ou de son modèle économique sans arbitrage.
- **Reprise** : relire le dernier registre, la version auditée et les décisions ; examiner les changements et impacts, conserver les identifiants et l'historique.

Respecter les autorisations déjà données. Préparer les éléments concrets avant un éventuel arbitrage. Une recommandation de mise en ligne, d'achat de domaine, de campagne ou de changement de prix n'autorise pas cette opération externe.

## Établir le diagnostic initial

Lire [la grille d'audit](references/grille-audit.md). Pour chaque domaine, consigner son applicabilité et son niveau d'examen : **examiné**, **partiellement examiné**, **non vérifié**, **non applicable**, avec motif et accès manquant. Ne pas appeler « audit complet » un contrôle limité aux fichiers README et au code. Un domaine examiné peut rester insatisfaisant ; ce statut décrit l'examen, pas sa réussite.

Effectuer les vérifications proportionnées : parcours réellement observés, captures d'interface si accessibles, lecture du code et des données, contrôles reproductibles, essais d'installation et de fonctionnement selon les accès. Une interface inaccessible limite les conclusions UX ; une compilation ne valide ni l'usage ni l'installation sur une autre machine. Employer des données d'essai adaptées et distinguer environnement local, préproduction et production.

Conserver un diagnostic **avant corrections**. Pour chaque constat matériel : ID stable `AUD-001`, domaine, observation, preuve et version, conséquence pour l'utilisateur ou l'exploitation, gravité motivée, recommandation et vérification attendue. Dédupliquer les symptômes d'une même cause. Enregistrer aussi les forces utiles à préserver. Distinguer défaut vérifié, hypothèse, demande nouvelle et préférence.

Les preuves peuvent être un fichier et une ligne, une capture contextualisée, une commande avec résultat et environnement, un scénario reproduit ou une source externe datée. Ne pas exposer de secrets ni de données personnelles dans le dossier. Sans reproduction ou accès suffisant, conserver une conclusion conditionnelle.

## Croiser les regards et arbitrer

Sur le même état initial, confronter utilisateur/métier, UX/accessibilité, produit, développement/architecture, qualité/sécurité, installation/exploitation, acquisition/vente. Faire ressortir les apports distincts, sans simuler une réunion d'experts ni compter leur accord comme des preuves indépendantes.

Rechercher l'objection la plus solide à une refonte ou une commercialisation proposée : besoin mal établi, coût de maintenance, alternative suffisante, dépendance fragile, absence de canal d'acquisition. Examiner aussi les forces et les améliorations peu coûteuses. Relier les arbitrages à l'objectif de l'utilisateur, pas à une architecture idéale.

Prioriser par conséquence, urgence réelle, fréquence, dépendances et effort plausible. Une gravité élevée doit avoir un scénario concret ; ne pas inventer un score global, des poids, une conformité, un taux de couverture ou une probabilité de vente. Distinguer gravité du constat et ordre de réalisation ; une dépendance peut passer avant un défaut plus grave.

Quand ils sont disponibles et pertinents, s'appuyer sur les skills d'UI/UX, de spécification, de sécurité, de livraison ou d'analyse critique pour approfondir leur domaine. Leur absence ne bloque pas la revue : effectuer les contrôles possibles et nommer les limites. Ne pas déléguer à des sous-agents sans autorisation applicable.

## Corriger et documenter dans le périmètre demandé

Pour une mise à niveau, lire [corrections et documentation](references/corrections-documentation.md). Relier chaque changement à un constat ou à une décision. Préserver le travail existant ; choisir une isolation adaptée. Ne pas changer les spécifications historiques pour faire disparaître un défaut.

Réaliser les corrections autorisées, les tests utiles et les mises à jour des spécifications, de l'architecture, de l'installation et de l'exploitation qu'elles affectent. Une proposition ou un fichier modifié n'est pas une correction vérifiée. Réauditer les parcours touchés et les dépendances plausibles ; distinguer réalisé, vérifié, partiellement vérifié, bloqué et différé.

Passer à la consolidation lorsque les contrôles prévus sont terminés et chaque constat prioritaire est corrigé et vérifié, ou documenté avec sa limite et sa prochaine action. Éviter une boucle de refonte sans fin. Un blocage sur la production ne doit pas empêcher les corrections locales indépendantes ni la remise d'un rapport provisoire.

## Préparer la visibilité et la commercialisation

Lire [visibilité et commercialisation](references/visibilite-commercialisation.md) lorsque ces domaines s'appliquent. Séparer maturité technique, utilité démontrée, visibilité et viabilité commerciale. Examiner le produit public, le site de présentation, les stores et le dépôt selon leur rôle ; le référencement d'une application locale n'est pas celui d'une page indexable.

Vérifier les données récentes et affirmations externes auprès de sources pertinentes et, pour les règles techniques ou exigences de plateformes, de sources officielles. Sans outils de recherche ou données commerciales, produire des hypothèses et un plan de validation, pas une étude de marché prétendument vérifiée.

Préparer les actions adaptées : site de présentation, documentation publique, démo, distribution, SEO, acquisition, mesure d'usage, support ou test de vente. Donner les prérequis, le livrable concret, le critère de réussite et la prochaine décision. Ne pas promettre un classement, du trafic ou des ventes.

## Livrer et maintenir le dossier

Lire [rapport et livrables](references/rapport-livrables.md). Produire à la fin de l'audit un **PDF**, sa source éditable, les constats, la traçabilité besoins–réalisation–tests et le plan d'actions. Les CSV dans [assets](assets/registre-constats.csv) fournissent des en-têtes réutilisables ; les adapter aux besoins sans casser les identifiants existants.

Après correction, le dossier doit montrer l'état initial, les changements réellement effectués, les vérifications finales et ce qui reste à faire. Conserver les décisions ouvertes et les réserves matérielles. Distinguer prêt à examiner, prêt à livrer, effectivement déployé et publié ; ne jamais déduire une publication d'un build réussi.

Utiliser le skill PDF s'il est disponible ou les outils documentaires présents. Vérifier le rendu, les coupures, les tableaux, la pagination et les liens utiles. Si la génération ou la lecture du rendu est impossible, remettre les sources, signaler précisément le livrable ou contrôle manquant et le moyen de terminer ; ne pas annoncer un PDF créé ou vérifié sans preuve.

Conclure avec les changements majeurs, le résultat des contrôles, les blocages matériels et les prochaines opérations ordonnées. Relier les fichiers effectivement produits et les versions concernées.
