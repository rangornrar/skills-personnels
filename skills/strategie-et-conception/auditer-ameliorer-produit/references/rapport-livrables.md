# Rapport, preuves et suivi

## Dossier attendu

Créer un dossier identifié par produit et date dans un emplacement approprié au projet. Ne pas remplacer un rapport historique sans conserver sa version. Conserver les fichiers de travail nécessaires pour reprendre l'audit.

| Livrable | Contenu |
| --- | --- |
| Rapport PDF | Synthèse décisionnelle, état initial, couverture de l'audit, constats sourcés, corrections, vérifications, limites et prochaines opérations |
| Source éditable | Rapport Markdown ou format documentaire maintenable ; sources et liens permettant de régénérer le PDF |
| Registre des constats | Identifiants stables, preuves, gravités motivées, corrections et statuts finaux |
| Matrice exigences | Exigences originales ou reconstituées, source, état observé, implémentation, tests et décisions |
| Plan d'actions | Actions ordonnées, constat associé, dépendances, rôle proposé, effort si estimable, critère de réussite et statut |
| Preuves et contrôles | Captures utiles, mesures, résumés de commandes et résultats, avec environnement/version et limites |

Pour initialiser les tableaux, utiliser les en-têtes des fichiers [constats](../assets/registre-constats.csv), [exigences](../assets/matrice-exigences.csv) et [actions](../assets/plan-actions.csv). Ne pas remplir un tableau avec des exemples présentés comme des faits. Des cellules « inconnu », « à estimer » ou « à attribuer » sont préférables à des valeurs inventées.

## Organisation du PDF

Adapter la longueur à la substance disponible ; pas de quota de pages. Ordre recommandé :

1. Couverture : produit, date, version/commit et modifications locales pertinentes, périmètre et statut provisoire ou consolidé.
2. Synthèse : utilité et état du produit, décisions prioritaires, forces, limites et recommandation conditionnelle de poursuite/livraison/vente.
3. Sommaire navigable si le document est long.
4. Objectifs et méthode : sources, environnements, accès, domaines examinés et lacunes.
5. Diagnostic initial par domaine : preuve, conséquence et correction proposée ; réserver les détails longs aux annexes.
6. Traçabilité avec le besoin initial et les décisions ultérieures.
7. Changements effectués et documents actualisés, liés aux constats.
8. Vérifications finales : réussites, échecs, contrôles non réalisés et risques résiduels.
9. Visibilité et commercialisation : données disponibles, hypothèses, alternatives et expériences proposées.
10. Plan des prochaines opérations : maintenant, après dépendances, à décider ; pas de calendrier fictif.
11. Annexes : registre détaillé, commandes utiles, architecture, preuves et sources datées.

Les liens et citations doivent permettre de retrouver la preuve pertinente. Pour un code local, donner chemin relatif au dépôt, version et ligne utile ; pour une source externe, titre, URL et date de consultation si elle compte. Ne pas inclure de clé, token, donnée utilisateur ou journal sensible. Identifier la version à laquelle chaque preuve s'applique.

## Produire et vérifier

Choisir une chaîne de génération compatible avec l'environnement : outils PDF ou documentaires présents, ou conversion depuis une source maintenable. L'absence d'un outil particulier ne justifie pas d'annoncer un fichier inexistant ; livrer les sources et expliquer le blocage si aucun moyen de génération n'est disponible.

Après génération, contrôler le texte extrait et le rendu visuel. Vérifier notamment caractères accentués, pages vides involontaires, titres isolés, marges, tableaux coupés, légendes, sources, pagination et sommaire. Inspecter les pages denses et les annexes ; le succès d'un export seul ne valide pas leur lisibilité. Après modification de mise en page, revérifier les pages affectées.

Un rapport final ne doit pas confondre « examen effectué », « produit satisfaisant », « correction réalisée », « vérification réussie » et « acceptation utilisateur ». Une restriction d'accès doit rester visible dans la synthèse si elle change la conclusion.

## Reprise et clôture

Réutiliser `AUD-xxx`, les identifiants d'exigences existants et `ACT-xxx` pour les actions. Ne pas renuméroter pour masquer l'historique. Relier constat → décision éventuelle → changement → contrôle → état final. Les actions de lancement restent ouvertes tant que leur résultat n'est pas constaté.

Le message de remise indique les fichiers réellement disponibles, les changements majeurs, les contrôles terminés et le prochain bloc d'actions. Si le PDF est provisoire ou non inspecté visuellement, le dire explicitement.
