import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import copy

#fonction qui doit etre mis dans la classe Graph de function.py
def build_complete_graph(self):
    G = nx.DiGraph()
    for i in range(len(self.matrix_ordonnacement)): #On creer les noeuds
        G.add_node(i)
    for num_ligne,ligne in enumerate(self.matrix_ordonnacement):
        for num_colonne,duration in enumerate(ligne):
            if type(duration)==int: #si ce n'est pas une étoile
                
                G.add_edge(num_ligne,num_colonne,duration=duration)

    #Position DAG
    #pos = nx.multipartite_layout(G, subset_key="layer")

    #Position circulaire
    """
    center_node = 4
    edge_nodes = set(G) - {center_node}
    pos = nx.circular_layout(G.subgraph(edge_nodes))
    pos[center_node] = np.array([0, 0])  # manually specify node position
    """

    #position spring
    pos  = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=400, arrowstyle='-|>', arrowsize=10)
    edge_weights = nx.get_edge_attributes(G, 'duration')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights,font_size=5,label_pos=0.7)


    #plt.savefig(str(txt), dpi=1200)  # Sauvegarde en PNG avec haute résolution
    plt.show()