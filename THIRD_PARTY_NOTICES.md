# Sources et attributions

## Créations et reprises personnelles

Les onze nouveaux skills et les fichiers de bibliothèque sont sous licence MIT ; le texte figure dans [LICENSE](LICENSE).

Les trois skills repris sont les copies locales de référence disponibles le 30 octobre 2026 :

- [analyse-critique-decision](https://github.com/rangornrar/analyse-critique-decision), avec sa licence et ses ressources locales.
- [concevoir-ameliorer-ui-ux](https://github.com/rangornrar/concevoir-ameliorer-ui-ux).
- [specifier-projet](https://github.com/rangornrar/specifier-projet), dont le choix de licence MIT est conservé pour cette bibliothèque.

Leurs fichiers de skill n'ont pas été réécrits pendant le regroupement. Les guides du dépôt individuel `specifier-projet` sont repris dans `docs/specifier-projet` avec adaptation des chemins et de la commande de validation à la bibliothèque.

## Imports OpenAI

Source : [openai/skills](https://github.com/openai/skills), révision [`49f948faa9258a0c61caceaf225e179651397431`](https://github.com/openai/skills/commit/49f948faa9258a0c61caceaf225e179651397431), récupérée le 30 octobre 2026.

| Skill | Répertoire source | Licence conservée |
| --- | --- | --- |
| gh-fix-ci | `skills/.curated/gh-fix-ci` | [Apache 2.0](skills/developpement/gh-fix-ci/LICENSE.txt) |
| gh-address-comments | `skills/.curated/gh-address-comments` | [Apache 2.0](skills/developpement/gh-address-comments/LICENSE.txt) |
| security-best-practices | `skills/.curated/security-best-practices` | [Apache 2.0](skills/securite/security-best-practices/LICENSE.txt) |
| security-threat-model | `skills/.curated/security-threat-model` | [Apache 2.0](skills/securite/security-threat-model/LICENSE.txt) |

Les fichiers amont importés sont conservés sans modification. Un `README.md` français a été ajouté localement dans chacun des quatre dossiers pour expliquer le but, le fonctionnement et les livrables ; ces guides locaux sont sous licence MIT et ne remplacent pas les instructions amont. La licence MIT racine ne remplace pas les licences des fichiers importés.

Les empreintes SHA-256 des fichiers importés, des trois reprises et des guides ajoutés figurent dans [sources.lock.json](sources.lock.json). Le champ `local_additions` distingue les documentations locales des fichiers d'origine. Le README d'`analyse-critique-decision` a été réorganisé pour présenter l'usage et les sorties avant l'installation ; cette adaptation et son empreinte d'origine sont déclarées dans `local_modifications`. Les deux autres reprises ont reçu un guide local. Les instructions des skills restent inchangées. Les empreintes détectent les changements ; elles ne constituent pas une signature de l'éditeur.

Pour mettre à jour un import, récupérer une révision explicite, examiner les changements et avis de licence, puis actualiser catalogue et empreintes. Ne pas corriger silencieusement les fichiers importés tout en les déclarant inchangés.
