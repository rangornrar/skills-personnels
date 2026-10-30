# Analyse critique et aide à la décision

Un skill en français pour confronter les hypothèses, comparer les options et formuler une recommandation argumentée, adaptée aux enjeux.

Il fournit une méthode de travail réutilisable à un assistant compatible avec les skills. Il ne modifie pas le modèle et ne garantit pas l'exactitude de ses réponses.

## Sommaire

- [À quoi cela sert](#à-quoi-cela-sert)
- [Comment l'utiliser](#comment-lutiliser)
- [Sorties attendues](#sorties-attendues)
- [Installation](#installation)
- [Fonctionnement détaillé](#fonctionnement-détaillé)
- [Architecture et ressources](#architecture-et-ressources)
- [Limites et contrôles](#limites-et-contrôles)
- [Licence](#licence)

## À quoi cela sert

- Distinguer les faits vérifiés, les informations rapportées, les hypothèses et les inconnues.
- Examiner les points de vue pertinents : technique, exploitation, finances, humain, organisation ou autres selon le sujet.
- Tester l'objection la plus solide et défendre honnêtement l'alternative sérieuse.
- Comparer les coûts complets, risques, délais, dépendances et possibilités de retour en arrière.
- Éviter la validation automatique, les scores arbitraires et le faux équilibre entre opinion et preuve.
- Recommander une action concrète et préciser les conditions qui feraient changer d'avis.

L'analyse reste courte pour les décisions simples. Le skill n'est pas destiné aux corrections de texte, traductions ou questions factuelles isolées.

## Comment l'utiliser

Indiquer si possible : l'objectif, les options envisagées, les contraintes impératives, le budget, l'échéance et les inconnues. Ajouter les documents utiles ou demander une vérification des sources si le sujet le nécessite.

### Exemples de demandes

#### Choix d'architecture IT

> Utilise $analyse-critique-decision pour comparer un monolithe modulaire et des microservices. Nous sommes cinq développeurs, avec peu de capacité d'exploitation et une livraison attendue dans six mois. Examine les compromis et ce qui justifierait de revoir le choix.

#### Mettre un projet à l'épreuve

> Utilise $analyse-critique-decision pour examiner ce plan. Cherche son hypothèse la plus fragile, l'objection principale et un test peu coûteux avant de nous engager : [plan].

#### Arbitrage professionnel

> Utilise $analyse-critique-decision pour comparer ces trois propositions. Mes priorités sont le délai, le coût total sur trois ans et la réversibilité : [propositions]. Signale les informations manquantes qui peuvent changer la décision.

#### Décision simple

> Utilise $analyse-critique-decision pour m'aider à choisir entre ces deux options : [options et contraintes]. Réponds en dix lignes maximum.

## Sorties attendues

La restitution est adaptée aux enjeux : une décision simple peut recevoir une réponse courte ; un arbitrage complexe peut justifier un tableau ou un dossier plus développé.

| Sortie | Contenu | Condition |
| --- | --- | --- |
| Recommandation argumentée | Option retenue, raisons et compromis déterminant. | Quand les informations permettent de trancher. |
| Comparaison des options | Avantages, limites, coûts complets, risques et réversibilité. | Tableau si cela facilite la décision. |
| Réserves et questions | Hypothèses, inconnues matérielles et ce qui ferait changer la conclusion. | Selon les limites des sources. |
| Prochaine action | Vérification, essai ou étape proportionnée pour avancer. | Proposée sans exécution externe implicite. |

Le skill produit d'abord une analyse dans la conversation. Un document ou un format de fichier particulier doit être demandé et dépend des outils disponibles.

## Installation

Suivre le [guide d'installation de la bibliothèque](../../../README.md#installer-les-skills-utiles), qui distingue ChatGPT sur le site web, le skill-installer de Codex et la copie locale.

Depuis la racine d'une copie locale de la bibliothèque, il est possible de préparer puis d'appliquer la copie de ce seul skill :

```sh
python scripts/install_local.py --skill analyse-critique-decision
python scripts/install_local.py --skill analyse-critique-decision --apply
```

Le script refuse d'écraser un dossier déjà présent. Utiliser ensuite le skill dans le client où il est installé, ou suivre la méthode par projet ChatGPT décrite dans le guide général.

## Fonctionnement détaillé

Le skill mobilise des rôles complémentaires selon la question :

| Rôle | Ce qu'il examine |
| --- | --- |
| Optimiste | Les opportunités, les forces et les conditions de réussite |
| Analyste factuel | Les faits chiffrés ou qualitatifs, leurs sources et les inconnues |
| Stratège | Le but à atteindre, les priorités, l'horizon et le coût d'opportunité |
| Contradicteur | L'objection principale, les scénarios d'échec et l'alternative sérieuse |
| Statisticien | Les données comparables, les taux de base, la variabilité et l'incertitude |
| Arbitre | Le choix recommandé, les compromis et les conditions de révision |

Pour une décision simple, deux ou trois angles utiles suffisent, arbitrage compris. Pour une décision importante, les rôles pertinents sont mobilisés ; l'examen statistique est ajouté si les données ou la question le justifient. Sans données adéquates, le skill doit dire que les chances de réussite ne sont pas estimables de manière fiable.

Les rôles partagent les mêmes faits. L'arbitre pèse les arguments selon les preuves et les priorités, sans vote majoritaire ni consensus forcé. Les désaccords importants restent visibles. Plusieurs personas d'un même modèle ne sont pas plusieurs expertises indépendantes.

Il s'agit d'une méthode d'examen, pas d'un dialogue théâtral ni d'un affichage du raisonnement interne détaillé. Par défaut, la réponse présente les conclusions utiles. Pour voir explicitement les contributions, demander :

> Utilise $analyse-critique-decision pour analyser ce projet. Présente les apports des six rôles, puis la recommandation de l'arbitre. Ne chiffre les chances de réussite que si les données le permettent : [contexte].

## Architecture et ressources

| Ressource | Rôle |
| --- | --- |
| [README.md](README.md) | Guide utilisateur : usage, sorties et installation. |
| [SKILL.md](SKILL.md) | Instructions suivies par l’assistant et critères de déclenchement. |
| [agents/openai.yaml](agents/openai.yaml) | Nom affiché, invite de départ et métadonnées d’interface. |
| [assets/](assets) | Icônes ou ressources utilisées par le skill. |

### Documentation complémentaire

- [Créer et utiliser des skills — documentation OpenAI](https://learn.chatgpt.com/docs/build-skills)
- [Skills dans ChatGPT — aide OpenAI](https://help.openai.com/fr-fr/articles/20001066-skills-in-chatgpt)

Les interfaces et les règles d'installation peuvent évoluer ; vérifier ces références en cas de différence avec l'application utilisée.

### Contribution

Ouvrir une issue ou une pull request avec un cas concret, le comportement observé et le résultat souhaité. Utiliser des exemples anonymisés. Privilégier les améliorations qui renforcent la qualité des preuves et des arbitrages sans allonger inutilement les réponses.

## Limites et contrôles

- Les résultats dépendent du modèle, du contexte et des outils autorisés. Sans accès aux sources, une vérification externe peut être impossible ; le skill demande de le signaler.
- Examiner plusieurs angles avec un seul assistant ne constitue pas une expertise indépendante de plusieurs professionnels.
- Une méthode critique ne supprime pas les erreurs, les biais ou les informations manquantes.
- Une recommandation ne vaut pas autorisation d'agir à l'extérieur de la conversation.
- La validation a couvert la structure du skill, un essai simple de comportement et un scénario de lancement B2B mobilisant les six rôles (intérêt déclaré, absence de paiements et budget limité). Elle ne constitue pas une évaluation systématique de la qualité des décisions.

## Licence

Distribué sous [licence MIT](LICENSE), autorisant l'utilisation, la modification et la redistribution, y compris commerciale, sous réserve de conserver les mentions de licence. Projet indépendant, sans affiliation ni approbation d'OpenAI.
