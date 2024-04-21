# Projet Theorie des graphes

Ce projet implémente un système de gestion de tâches avec des contraintes de précédence et de durée, utilisant un graphe pour visualiser et analyser les dépendances entre tâches.

## Fonctionnalités

- Lecture des tâches et de leurs contraintes à partir d'un fichier txt.
- Construction d'un graphe de tâches incluant des nœuds pour chaque tâche et des arêtes représentant les contraintes de précédence.
- Analyse de la possibilité de cycles dans le graphe, ce qui pourrait indiquer des contraintes de précédence conflictuelles.
- Calcul du rangs de tous les sommets du graphes Calcul des dates les plus tôt et les plus tard de chaque tâche, les marges, Ainsi que le calcul de chemin(s) critique(s).
- Visualisation du graphe avec les durées des tâches et les relations de dépendance.

## Dépendances

Ce projet nécessite les bibliothèques Python suivantes :
- `numpy`
- `networkx`
- `matplotlib`
- `pandas`

## Installation

Assurez-vous que Python est installé sur votre système. Ensuite, installez les dépendances nécessaires en exécutant :

```bash
pip install numpy networkx matplotlib pandas

en fonction de votre version de python cela peut être aussi 

py -m pip install numpy networkx matplotlib pandas
ou 
python -m pip install numpy networkx matplotlib pandas