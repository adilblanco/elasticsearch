## 1. Corpus
___

| document | text |
| :---     | ---:    |
| D1       | Map Reduce est un patron de conception de développement informatique, inventé par Google, dans lequel sont effectués des calculs parallèles, et souvent distribués, de données potentiellement très volumineuses, typiquement supérieures en taille à un téraoctet.      |
| D2       | Les termes « map » et « reduce », et les concepts sous-jacents, sont empruntés aux langages de programmation fonctionnelle utilisés pour leur construction (map et reduce de la programmation fonctionnelle et des langages de programmation tableau).|
| D3       | Il permet de manipuler de grandes quantités de données en les distribuant dans un cluster de machines pour être traitées. Ce modèle connaît un vif succès auprès de sociétés possédant d'importants centres de traitement de données telles Amazon et Facebook.|
| D4       | Map Reduce commence aussi à être utilisé au sein du Cloud computing. De nombreux framework ont vu le jour afin d'implémenter le Map Reduce. Le plus connu est Hadoop qui a été développé par Apache Software Foundation et Google était à l’origine du Map Reduce.|
| D5       | Ces framework possèdent des inconvénients qui réduisent considérablement ses performances notamment envmilieu hétérogène. Des framework permettant d'améliorer les performances de Hadoop et les performancesvglobales, tant en termes de vitesse de traitement qu'en consommation électrique, commencent à voir le jour.|
| D6       | C’est un modèle de programmation popularisé par Google. Il est principalement utilisé pour la manipulation et le traitement d’un nombre important de données au sein d’un cluster de noeuds.|

## 2. Calcul TF-IDF
___

| term      | document| corpus | terms  | binaire      | frequence | log(n + 1) | normal | TF     | DF    | IDF    | TF * IDF |
| :---      | :----:  | :----: | :----: |  :----:      |  :----:   |  :----:    | :----: | :----: | :----:|  :----:| ---:     |
| google    | D1      | 6      | 35     |<mark>1</mark>| 1         | log(2)     | 1/35   | log(2) | Tit   | Here   | bb       |
| framework | D1      | 6      | 35     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | aa       |
| map       | D1      | 6      | 35     |<mark>1</mark>| 1         | log(2)     | 1/35   | log(2) | Tit   | Here   | bb       |
| et        | D1      | 6      | 35     |<mark>1</mark>| 1         | log(2)     | 1/35   | log(2) | Tit   | Here   | aa       |
| google    | D2      | 6      | 34     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| framework | D2      | 6      | 34     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | aa       |
| map       | D2      | 6      | 34     |<mark>1</mark>| 2         | log(3)     | 2/34   | log(3) | Tit   | Here   | bb       |
| et        | D2      | 6      | 34     |<mark>1</mark>| 4         | log(5)     | 4/34   | log(5) | Tit   | Here   | aa       |
| google    | D3      | 6      | 41     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| framework | D3      | 6      | 41     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | aa       |
| map       | D3      | 6      | 41     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| et        | D3      | 6      | 41     |<mark>1</mark>| 1         | log(2)     | 1/41   | log(2) | Tit   | Here   | aa       |
| google    | D4      | 6      | 47     |<mark>1</mark>| 1         | log(2)     | 1/47   | log(2) | Tit   | Here   | bb       |
| framework | D4      | 6      | 47     |<mark>1</mark>| 1         | log(2)     | 1/47   | log(2) | Tit   | Here   | aa       |
| map       | D4      | 6      | 47     |<mark>1</mark>| 3         | log(4)     | 3/47   | log(4) | Tit   | Here   | bb       |
| et        | D4      | 6      | 47     |<mark>1</mark>| 1         | log(2)     | 1/47   | log(2) | Tit   | Here   | aa       |
| google    | D5      | 6      | 43     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| framework | D5      | 6      | 43     |<mark>1</mark>| 2         | log(3)     | 2/43   | log(3) | Tit   | Here   | aa       |
| map       | D5      | 6      | 43     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| et        | D5      | 6      | 43     |<mark>1</mark>| 1         | log(2)     | 1/43   | log(2) | Tit   | Here   | aa       |
| google    | D6      | 6      | 32     |<mark>1</mark>| 1         | log(2)     | 1/32   | log(2) | Tit   | Here   | bb       |
| framework | D6      | 6      | 32     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | aa       |
| map       | D6      | 6      | 32     | 0            | 0         | log(1)     | 0      | log(1) | Tit   | Here   | bb       |
| et        | D6      | 6      | 32     |<mark>1</mark>| 1         | log(2)     | 1/32   | log(2) | Tit   | Here   | aa       |
