import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


# Lecture du tableau de contraintes depuis un fichier texte
def read_file(file_name):
    tableau = []
    with open(file_name, 'r') as f:
        for line in f:
            tache = list(map(int, line.strip().split()))
            tableau.append(tache)
    return tableau

def build_class(tableau):
    tabTask = [i+1 for i in range(len(tableau))]
    for i in range(len(tableau)):
        tabTask[i] = Task(tableau[i])

    return tabTask



class Task:

    def __init__(self, ligne):
        self.index = ligne[0]
        self.duration = ligne[1]
        self.predecessors = [] # tableau de Task
        self.succesors = []  #tableau de 
        self.rank = None 

    def add_predecessors(self,task):
        self.predecessors.append(task)
    def add_successors(self,task):
        self.succesors.append(task)







    
class Graph:

    def __init__(self,tabTask):
        self.tabTask = tabTask #tableau de Task
        self.task_init = Task([0,0]) 
        self.task_end = Task[(len(tabTask)+1),0] #dernier element de la liste (n+1)
        self.cycle = None

    def build_predecessors(self,tableau):
        int_predecessors = [ligne[2:] for ligne in tableau ] #creation d'un tableau d'entier de predecesseur
        for i in range(len(int_predecessors)):
            for el in int_predecessors[i]:
                self.tabTask[i].add_predecessors(self.tabTask[el-1])


    def build_succesors(self,tableau): #creer les successeurs des taches
        int_predecessors = [ligne[2:] for ligne in tableau ] #creation d'un tableau d'entier de predecesseur
        for i in range(len(int_predecessors)):
            for j in range(len(int_predecessors)):
                if (i+1) in int_predecessors[j]: #s'il y a son index dans une des liste des predecesseurs c'est son successeur 
                    self.tabTask[i].add_successors(self.tabTask[j])

    def build_init(self): #initie le/s succeseurs d'alpha et mes à jours les predecesseurs de ces successeurs
        without_predecessors = [] #element qui n'ont pas de predecesseurs
        for i in range(len(self.tabTask)):
            if len(self.tabTask[i].predecessors)==0 :
                self.task_init.add_successors(self.tabTask[i])
                self.tabTask[i].add_predecessors(self.task_init)

    def build_end(self): #creer la tache de fin et met à jours successeur et predecesseurs
        pass #en cours

def build_graph(tableau):
    G = nx.DiGraph()
    for tache in tableau:
        noeud = tache[0]
        poids = tache[1]
        G.add_node(noeud, weight=poids) #Ajoute le noeud avec son poids
        for dep in tache[2:]:
            G.add_edge(dep, noeud)
    # Dessiner le graphe
    pos = nx.spring_layout(G)  # Position des noeuds utilisant l'algorithme de Fruchterman-Reingold
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True) if 'weight' in d])

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    print(G.out_edges(8))
    plt.show()
    return G

