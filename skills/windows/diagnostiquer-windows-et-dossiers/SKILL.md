---
name: diagnostiquer-windows-et-dossiers
description: "Diagnostiquer un problème Windows lié aux fichiers, dossiers, disques, permissions ou applications, et comparer des arborescences après copie ou clonage. Utiliser pour une enquête technique et une correction justifiée ; ne pas déclencher pour supprimer des données sans diagnostic ni pour livrer une application depuis son code."
---

# Diagnostiquer Windows avec des preuves

Commencer par la cible exacte, le symptôme, le contexte de copie ou de clonage et le résultat attendu. Lire les journaux et éléments disponibles. Déduire ce qui peut l'être avant de poser des questions ; ne pas confondre chemin affiché, chemin résolu et contenu réellement visé.

## Examiner avant de corriger

- Inventorier les volumes et chemins pertinents, types de fichiers, attributs, propriétaires, ACL et points de jonction selon le symptôme.
- Vérifier si le chemin appartient au système actif, à une ancienne installation, à une sauvegarde ou à un espace synchronisé. Un nom « Windows » sur un autre disque ne suffit pas à établir son rôle.
- Pour une erreur d'accès, distinguer droits insuffisants, fichier utilisé, chiffrement, lien, synchronisation et problème matériel. Ne pas attribuer la cause à l'antivirus sans preuve.
- Pour un diagnostic de logiciel, identifier version, erreur, configuration et changements récents avant de réinstaller ou de supprimer sa configuration.

## Comparer des dossiers

Définir le sens de comparaison et les exclusions. Commencer par chemins relatifs, tailles et dates ; pour confirmer l'identité, utiliser les empreintes des contenus pertinents. Une date différente ne prouve pas un contenu différent. Séparer fichiers absents, supplémentaires, identiques et différents.

Ne pas suivre récursivement les jonctions ou liens sans stratégie explicite : éviter boucles et sorties de périmètre. Indiquer les fichiers illisibles ou instables pendant la comparaison. Un rapport sans erreur de lecture ne signifie pas que toutes les variantes de métadonnées ont été comparées.

## Proposer une correction proportionnée

Relier la correction à la cause établie et expliquer son effet. Préférer une modification ciblée et réversible ; conserver les permissions et configurations d'origine utiles à un retour arrière. Ne pas prendre possession de tout un disque pour résoudre le problème d'un seul dossier.

Avant une suppression ou un déplacement récursif, résoudre et vérifier la cible absolue dans le périmètre explicitement nommé. Utiliser un seul shell de bout en bout et des opérations natives avec chemins littéraux. Ne pas construire des commandes de suppression par concaténation de noms non contrôlés ni masquer un refus d'accès en changeant d'outil.

Respecter les autorisations et garde-fous de l'environnement pour toute mutation. Ne pas désactiver une protection de sécurité ou modifier une stratégie d'accès pour contourner un blocage. En cas de refus, collecter les preuves utiles et proposer la prochaine étape autorisée.

## Vérifier et restituer

Contrôler le symptôme après correction et vérifier les effets sur la cible. Livrer un rapport compact : constat, cause démontrée ou hypothèses restantes, actions réalisées, résultat, fichiers exclus ou illisibles et retour arrière disponible. Ne pas présenter une opération lancée en arrière-plan comme terminée.
