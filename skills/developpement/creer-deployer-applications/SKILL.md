---
name: creer-deployer-applications
description: "Concevoir et réaliser une application de bout en bout : besoin, choix des plateformes et de l'architecture, maquettes, développement, tests et déploiement. Utiliser pour transformer une idée en application mobile, de bureau ou web, ou reprendre un projet sur plusieurs de ces étapes. Ne pas déclencher pour un bug isolé, une simple question technique ou une demande limitée à un document de spécifications."
---

# Créer et déployer une application

Répondre en français sauf demande contraire. Accompagner la réalisation du produit demandé, avec une démarche proportionnée à sa taille. Ne privilégier aucune plateforme, stack, architecture ou solution d'hébergement avant d'avoir compris les usages. Une application locale sans compte, sans serveur et sans abonnement peut être la bonne solution.

## Entrer au bon endroit

- Lire les instructions du dépôt, les fichiers, les changements locaux, les spécifications et les décisions disponibles. Vérifier que le dossier courant correspond au produit demandé ; un répertoire ouvert ne définit pas à lui seul le besoin.
- Identifier le point d'entrée : idée à préciser, conception, prototype, réalisation, reprise ou livraison. Conserver ce qui est exploitable et commencer à la première incertitude déterminante ; ne pas rejouer les étapes terminées.
- Respecter la portée : une demande de maquettes conduit aux maquettes ; une demande de développement comprend le code et sa vérification ; une demande de bout en bout inclut la livraison dans les limites des accès et autorisations existants.
- Si le besoin est absent, demander le problème à résoudre, les utilisateurs et un exemple concret. Poser une à trois questions déterminantes à la fois. Lire les sources avant de questionner et avancer sur le travail indépendant des réponses.
- Ne pas choisir à la place de l'utilisateur un objectif métier, un budget ou une diffusion publique. Pour les choix techniques courants et réversibles, proposer un choix motivé puis avancer en explicitant l'hypothèse. Une absence de réponse ne constitue pas une approbation.

## Piloter par livrables

Pour une demande complète, couvrir les étapes ci-dessous dans l'ordre de leurs dépendances ; revenir seulement sur les décisions affectées par un fait nouveau. Ne pas demander une autorisation à chaque étape et ne pas s'arrêter à un plan lorsque la réalisation est demandée.

| Étape | Résultat concret attendu |
| --- | --- |
| Besoin | Problème, utilisateurs, parcours principal, périmètre de première version et critères de réussite observables. |
| Cible et architecture | Plateformes et canaux de diffusion retenus, stack motivée, composants, données, intégrations et contraintes de construction. |
| Maquettage | Parcours, écrans et états essentiels, maquette consultable et interactions explicites. |
| Réalisation | Première tranche utilisable de bout en bout, puis fonctions prioritaires intégrées et documentation utile. |
| Vérification | Contrôles appropriés, parcours exercés sur les cibles accessibles, défauts corrigés et limites identifiées. |
| Livraison | Artefact installable ou service déployé selon la cible, instructions, preuve de vérification et dispositif de mise à jour adapté. |

Un livrable peut rester provisoire. Distinguer une hypothèse de travail, une recommandation, un choix explicite de l'utilisateur et un résultat vérifié. Ne pas fabriquer de validation utilisateur ou de test sur un appareil inaccessible.

## Tenir un état de reprise

Dès que le projet est suffisamment défini, maintenir un état compact dans ses documents existants ou, à défaut, dans `docs/projet/etat.md`. Lire [suivi-projet.md](references/suivi-projet.md) pour le contenu et les modalités de reprise. Créer ce suivi dans le projet concerné, pas dans un dépôt sans rapport.

Conserver les besoins, décisions, preuves et prochaines actions utiles ; éviter de multiplier les fichiers pour une petite application. Séparer la documentation du produit des notes temporaires. À chaque jalon ou interruption utile, actualiser l'état et le prochain travail exécutable.

## Définir le besoin et choisir la cible

Lire [cadrage-architecture.md](references/cadrage-architecture.md) pendant le cadrage, le choix de plateforme ou une décision technique structurante.

- Partir du parcours métier, des appareils disponibles et de la distribution souhaitée. Distinguer plateforme prioritaire et cibles ultérieures ; ne pas déduire « toutes les plateformes » d'une liste d'exemples.
- Comparer natif, multiplateforme ou web/PWA uniquement lorsque l'arbitrage est réel. Relier la recommandation aux API nécessaires, à l'usage hors ligne, à l'intégration système, aux compétences et à la maintenance.
- Vérifier tôt les obstacles de faisabilité : matériel ou service de construction, SDK, appareil d'essai, signature, comptes et accès aux stores ou à l'hébergement. Distinguer ce qui peut être développé ici de ce qui peut être construit, signé, installé et publié ici.
- Pour les capacités, compatibilités, versions, coûts et règles de diffusion actuels, consulter les sources officielles pertinentes et noter les liens et dates utiles. Ne pas figer ces informations dans le skill.
- Avant d'investir dans une intégration centrale incertaine, réaliser une courte preuve technique adaptée à la cible. Un aperçu dans un navigateur ne prouve pas la disponibilité d'une API native.

## Maquetter puis réaliser

Lire [maquettes-realisation.md](references/maquettes-realisation.md) pour produire le prototype, coder ou vérifier le produit.

- Construire le parcours et ses états avec des contenus représentatifs avant les détails décoratifs. Adapter les interactions à la plateforme et aux modes d'entrée.
- Produire des maquettes concrètes et, si cela aide à examiner le parcours, un prototype navigable. Choisir le format adapté aux outils et au besoin ; une image seule ne démontre pas une interaction.
- Implémenter une première tranche qui relie interface, logique et persistance ou intégration réellement nécessaires. Étendre ensuite par scénarios prioritaires, avec les erreurs et reprises utiles.
- Réutiliser les conventions et composants existants. Choisir une architecture proportionnée ; ne pas ajouter un serveur, une authentification, des microservices ou une dépendance sans besoin.
- Relier la vérification aux critères de réussite. Vérifier le rendu réel lorsque possible ; séparer tests automatiques, contrôles d'interface, tests sur émulateur et tests sur appareil.

## Livrer, déployer et permettre la maintenance

Lire [livraison-exploitation.md](references/livraison-exploitation.md) avant de préparer une distribution, un déploiement ou une mise à jour.

Préparer complètement les artefacts et vérifications accessibles avant une éventuelle demande d'action utilisateur. Réutiliser l'autorisation déjà donnée si elle couvre l'environnement, la cible et l'action. Une demande de préparation au déploiement n'autorise pas une publication publique, un achat ou un abonnement. Si une décision ou un accès manque, préciser uniquement cet élément et continuer le travail indépendant.

Ne pas annoncer « déployé » après un simple build, ni « publié » après une soumission en cours de revue. Vérifier l'état réel et le parcours essentiel sur l'environnement livré lorsque possible. En cas de blocage externe, remettre le livrable disponible, la limite précise et la procédure restante ; laisser l'étape correspondante ouverte.

## Utiliser les spécialisations à bon escient

Ce skill reste utilisable seul. Selon la tâche et leur disponibilité :

- `specifier-projet` pour un entretien approfondi ou un dossier de spécifications ; ne pas l'activer automatiquement si son processus documentaire dépasserait le besoin.
- `concevoir-ameliorer-ui-ux` pour approfondir les usages et la conception ; les capacités de Product Design pour des variantes ou une implémentation fidèle si elles sont pertinentes et disponibles.
- Les skills de création web, documents, PDF et autres formats uniquement lorsque le livrable demandé en relève.
- `auditer-ameliorer-produit` pour une revue globale d'un produit existant, pas pour imposer un audit complet à chaque itération.

Lire les instructions de la spécialisation avant usage et annoncer son emploi selon les règles de l'environnement. Son absence ne bloque pas les travaux réalisables. Ne pas introduire de sous-agents sans autorisation applicable.

## Restituer l'avancement

Présenter le résultat concret, les fichiers ou artefacts consultables, les vérifications réalisées et les limites matérielles. Mettre en évidence la prochaine action ou décision seulement si elle reste nécessaire. Pour un projet partiel, ne pas présenter tout le cycle comme terminé. Pour un projet livré, préciser la version, la cible et le canal effectivement disponibles.
