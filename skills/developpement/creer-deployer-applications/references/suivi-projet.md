# État du projet et continuité

Lire lors d'une création ou reprise du suivi. Réutiliser les spécifications, ADR, tickets et documents existants plutôt que créer un système parallèle.

## État compact

À défaut d'organisation existante, utiliser `docs/projet/etat.md`. N'y conserver que le nécessaire à une reprise fiable :

- Produit, objectif, utilisateurs et périmètre de première version.
- Phase et scénario en cours ; livrables disponibles avec chemins ou liens.
- Cibles initiales et ultérieures, stack, environnements de build, de test et de diffusion.
- Décisions structurantes et source : utilisateur, contrainte vérifiée ou hypothèse réversible ; date utile et motif.
- Scénarios prioritaires et critères de réussite, avec lien vers leur détail s'il existe.
- État de réalisation et preuves de vérification, avec version ou commit si disponible.
- Questions, risques et blocages matériels : conséquence et élément nécessaire pour avancer.
- Prochaine action concrète et autorisations externes utiles déjà données, avec leur portée.

Employer des identifiants stables pour les exigences ou décisions qui doivent être reliées aux tests. Ne pas imposer une numérotation complète pour une application minuscule.

Séparer les statuts :
- Besoin ou décision : proposé, hypothèse, décidé explicitement, à clarifier.
- Travail : à faire, en cours, réalisé, vérifié, bloqué ou différé.
- Livraison : préparée, construite, signée si applicable, distribuée, soumise, publiée ou déployée.

Ces statuts ne sont pas interchangeables. La phase suivante ne rend pas automatiquement la précédente approuvée ; une preuve de build ne vaut pas preuve d'installation.

## Documents à ajouter seulement s'ils servent

Selon l'ampleur, conserver séparément besoin et recette, architecture et décisions, maquettes, instructions d'installation et exploitation. Markdown suffit par défaut pour garder des sources modifiables. Produire un PDF ou autre format lorsque demandé ou pertinent, avec le skill du format et sa vérification.

Ne pas générer tous les documents comme des coquilles vides à l'ouverture du projet. Mettre à jour les documents touchés par les décisions et le code ; ne pas réécrire l'historique pour masquer un écart.

## Reprise après interruption

1. Relire le suivi et les sources qu'il désigne.
2. Vérifier l'état réel : fichiers et changements, outillage, livrables, tests et déploiement accessibles.
3. Résoudre les écarts entre notes et produit sans effacer les décisions antérieures ; préciser une nouvelle preuve lorsqu'elle change une hypothèse.
4. Reprendre la prochaine action indépendante ; demander seulement l'information manquante qui empêche réellement une décision ou une exécution.

Un résumé antérieur est un point de départ, pas une preuve actuelle. Ne pas recommencer l'entretien ou réinventer la stack si les décisions et contraintes restent valables.
