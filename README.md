# Projet Theorie des graphes

Ce projet implémente un système de gestion de tâches avec des contraintes de précédence et de durée, utilisant un graphe pour visualiser et analyser les dépendances entre tâches.
![alt text](https://github.com/raphber94/Theorie_graphes/blob/main/graph_layout/14.png)

(pour le txt 14 )
```bash
1 1
2 2
3 3 1
4 4 1 2
5 5 2 4
```

avec pour 1er élèment la tache le 2nd la durée et les autres ses prédecesseurs
## Fonctionnalités

- Lecture des tâches et de leurs contraintes à partir d'un fichier txt.
- Construction d'un graphe de tâches incluant des nœuds pour chaque tâche et des arêtes représentant les durées de précédence.
- Analyse de la possibilité de cycles dans le graphe
- Calcul du rangs de tous les tâches du graphes, calcul des dates les plus tôt et les plus tard de chaque tâche, les marges, Ainsi que le calcul de(s) chemin(s) critique(s).
- Visualisation du graphe avec les durées des tâches et les relations de dépendance.

## Dépendances

Ce projet nécessite les bibliothèques Python suivantes :
- `numpy`
- `networkx`
- `matplotlib`
- `pandas`
- `PIL`

## Installation

Assurez-vous que Python est installé sur votre système. Ensuite, installez les dépendances nécessaires en exécutant :

```bash
pip install numpy networkx matplotlib pandas

en fonction de votre version de python cela peut être aussi 

py -m pip install numpy networkx matplotlib pandas
ou 
python -m pip install numpy networkx matplotlib pandas
