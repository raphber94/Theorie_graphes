from functions import *
import pandas as pd
import numpy




while True:
    choice = '0'
    print("Merci de choisir un fichier de test à choisir")
    txt = int(input("Entrez votre choix de test"))
    if (txt>0 and txt <=14): # le choix est correcte on passe au choix suivant 
            
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
            print("5. Option 5")
            print("6. Quitter")
            choice = input("Entrez votre choix (1-6): ") 
        


    

    if choice == '1':
        print("Affichage de la matrice")
        for ligne in tableau:
            print(ligne)
    elif choice == '2':
        print("Affichage de la matrice d'ordonnacement comme un jeu de triplets ")
        graph.print_triplet()

    elif choice == '3':
        print("Affichage de la matrice d’ordonnancement sous forme de matrice des valeurs")
        graph.print_matrix()
    elif choice == '4':
        for i in graph.finaltabTask:
            print(type(i.succesors))
        print("Vous avez choisi l'option 4")
        print(graph.is_cyclic())
    elif choice == '5':
        print("Vous avez choisi l'option 5")
    elif choice == '6':
        print("Sortie du programme...")
        break
    else:
        print("Choix invalide")





### Print 

