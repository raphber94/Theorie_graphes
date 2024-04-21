from functions import *



while True:
    choice = '0'
    print("Merci de choisir un fichier de test à choisir")
    txt = int(input("Entrez votre choix de test "))
    if (txt>0 and txt <=15): # le choix est correcte on passe au choix suivant
            
            path = "fichier_test/"+str(txt)+".txt"
            tableau = read_file(path) #ne prend pour l'instant pas en compte la variable txt

            ### initialisation graph ###
            tabTask = build_class(tableau)
            graph = Graph(tabTask)
            graph.initialisation(tableau)


            print("\nMenu Principal")
            print("Tapez le numéro de l'option que vous souhaitez choisir:")
            print("1. Affichage de la matrice ")
            print("2. Affichage de la matrice d'ordonnacement comme un jeu de triplets ")
            print("3. Affichage de la matrice d’ordonnancement sous forme de matrice des valeurs")
            print("4. Cyclique")
            print("5. Rangs des tâches")
            print("6. Graphe d'ordonnancement et dates")
            print("7. Chemins critiques")
            print("8. Afficher le graphe graphiquement")
            print("9. Quitter\n")
            choice = input("Entrez votre choix (1-9):\n ")


    if choice == '1':
        print("Affichage de la matrice\n")
        for ligne in tableau:
            print(ligne)
    elif choice == '2':
        print("Affichage de la matrice d'ordonnacement comme un jeu de triplets \n")
        graph.print_triplet()

    elif choice == '3':
        print("Affichage de la matrice d’ordonnancement sous forme de matrice des valeurs\n")
        graph.print_matrix()
    elif choice == '4':
        print("Vous avez choisi l'option 4 \n")
        graph.is_cyclic(is_print=True)
    elif choice == '5':
        print("Rang du graphes...")
        if graph.is_cyclic():
            print("Le graph est  cyclique il n'est donc pas possible de calculer les rangs\n")
        else:
            graph.rank()
    elif choice == '6':
        print("Graphe d'ordonnancement...")
        if graph.is_cyclic():
            print("Impossible de faire de ce graphe un graphe d'ordonnancement car il est cyclique\n")
        else:
            graph.rank()
            graph.earliest_date()
            graph.latest_date()
            graph.margin()
    elif choice== '7':
        print("Chemins critiques")
        if graph.is_cyclic():
            print("Impossible de faire de ce graphe un graphe d'ordonnancement car il est cyclique")
        else:
            graph.rank()
            graph.earliest_date()
            graph.latest_date()
            graph.margin()
            graph.critical_path(temp_critical_path=[])
            graph.final_critical_path()
            print(graph.critical_path_tab)
            print(graph.maximal_critical_path)
    elif choice== '8':
        print("Affichage du graphe")
        format = "graph_layout/"+str(txt)+".png"
        image = Image.open(format)
        image.show()
    elif choice == '9':
        print("Sortie du programme...")
        break
    else:
        print("Choix invalide")





