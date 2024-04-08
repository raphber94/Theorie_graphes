from functions import *
tableau = read_file("test.txt")
for ligne in tableau:
    print(ligne)
afficher_graphe(tableau)
G = build_graph(tableau)
tritopologique_and_valeur_negative(G)

calendrier(tableau)