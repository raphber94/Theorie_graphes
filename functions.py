import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Création d'une classe graph
"""
class graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    # Fonction pour ajouter une arête au graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    # Fonction récursive pour le tri topologique
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)
    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)
"""
# Lecture du tableau de contraintes depuis un fichier texte
def read_file(file_name):
    tableau = []
    with open(file_name, 'r') as f:
        for line in f:
            tache = list(map(int, line.strip().split()))
            tableau.append(tache)
    return tableau


def afficher_graphe(tableau):
    # Trouver le nombre de tâches
    N = len(tableau)
    # Initialiser une matrice de taille (N+2)x(N+2) remplie de 0
    # On initialise la matrice à N+2 pour pouvoir y mettre le pt de départ et arrivé fictif
    matrice = [[0] * (N + 2) for i in range(N + 2)]

    # Remplir la matrice avec les durées de tâches et les contraintes
    for i in range(N):
        tache = tableau[i]
        matrice[tache[0]][tache[0]] = tache[1]
        for j in range(2, len(tache)):
            matrice[tache[j]][tache[0]] = tache[1]

    # Afficher la matrice
    for i in range(N + 2):
        for j in range(N + 2):
            print(matrice[i][j], end='\t')
        print()
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

def tritopologique_and_valeur_negative(G):
    nega = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True) if 'weight' in d] and d['weight']<0)
    if nega:
        print("Le graph contient des valeurs négatives", nega)
        return
    else:
        print("Le graph ne contient pas de valeur négatives", nega)
    try:
        topological_order = list(nx.topological_sort(G))
        print("Voici un ordre topologique de ce graphe", topological_order)
    except nx.NetworkXUnfeasible:
        print("Le graphe contient un cycle, le tri topologique n'est pas possible")

def parcours_en_largeur(s):
    


