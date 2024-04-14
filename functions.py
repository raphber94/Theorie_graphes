import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd


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
        self.tabTask = tabTask #tableau de Task NE CONTIENT PAS ALPHA ET TACHE DE FIN
        self.task_init = Task([0,0]) 
        self.task_end = Task([(len(self.tabTask)+1),0]) #dernier element de la liste (n+1)
        self.cycle = None
        self.finaltabTask = [] #init + tabTask + end

    def build_predecessors(self,tableau):
        int_predecessors = [ligne[2:] for ligne in tableau ] #creation d'un tableau d'entier de predecesseur
        for i in range(len(int_predecessors)):
            for el in int_predecessors[i]:
                self.tabTask[i].add_predecessors(self.tabTask[el-1])

    def build_finaltabTask(self):
        self.finaltabTask.append(self.task_init)
        self.finaltabTask.extend(list(self.tabTask))
        self.finaltabTask.append(self.task_end)

    def initialisation(self,tableau):
        self.build_predecessors(tableau)
        self.build_succesors(tableau)
        self.build_init()
        self.build_end()
        self.build_finaltabTask()

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
        without_successors = []
        for i in range(len(self.tabTask)):
            if len(self.tabTask[i].succesors)==0: #si une tache n'a pas de successeurs
                self.task_end.add_predecessors(self.tabTask[i])
                self.tabTask[i].add_successors(self.task_end)

    """
    #Fonctionne mais trop lourd
    #possibilité de refaire le code sans recursive avec 2 for
    def print_triplet(self,task: Task,liste_print): #Affichage du graphe comme un jeu de triplets parcours en largeur recusifs 
        print((len(self.tabTask)+2),"sommets")

    
    def recursive_triplet(self,task: Task,list_print):
        for i in range(len(task.succesors)):
            tostr = f"{task.index} -> {task.succesors[i].index} = {task.duration}"
            list_print.append(tostr)
            self.print_triplet(task.succesors[i],list_print) #repete la meme chose dans les successeurs 
    """
    def print_triplet(self): #etape 1
        print(len(self.finaltabTask),"sommets")
        count = 0
        for i in range(len(self.finaltabTask)):
            for j in range(len(self.finaltabTask[i].succesors)):
                print(self.finaltabTask[i].index," -> ",self.finaltabTask[i].succesors[j].index," = ",self.finaltabTask[i].duration)
                count += 1
        print(count,"arcs")

    def print_matrix(self): #etape 2
        matrix = []
        ligne = []
        past = False  
        for i in range(len(self.finaltabTask)):
            for j in range(len(self.finaltabTask)):
                past = False
                for k in self.finaltabTask[i].succesors: #si l'élément est un succéceur
                    if k.index == j : 
                        ligne.append(self.finaltabTask[i].duration) #ajout a la matrice de la duree
                        past = True
                
                if (not past): #j n'est aucun des successeurs
                    ligne.append("*")
                
            matrix.append(ligne)
            ligne = []
        
        labels=[i for i in range(len(self.finaltabTask))]
        df = pd.DataFrame(matrix, columns=labels, index=labels)
        print(df)

    def is_cyclic(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return  


    def rank(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return         

    def earliest_duration(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return 

    def longest_duration(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return 

    def overall_margin(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return 

    def critical_path(self):#Simple squelette, la fonction n'est pas terminé
        if not self.cycle :
            print("Le graph n'est pas cyclique il n'est pas possible de faire cela") 
            return 
        
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



