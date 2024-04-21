import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import copy
from PIL import Image
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
        self.earliest_date = None
        self.latest_date = None
        self.margin = None
        

    def add_predecessors(self,task):
        self.predecessors.append(task)
    def add_successors(self,task):
        self.succesors.append(task)
    def sup_predecessors(self,index):
        for i in range(len(self.predecessors)):
            if self.predecessors[i].index == index :
                self.predecessors.pop(i)
                break
    def sup_successors(self,index):
        for i in range(len(self.succesors)):
            if self.succesors[i].index == index :
                self.succesors.pop(i)
                break
     
        



class Graph:

    def __init__(self,tabTask):
        self.tabTask = tabTask #tableau de Task NE CONTIENT PAS ALPHA ET TACHE DE FIN
        self.task_init = Task([0,0]) 
        self.task_end = Task([(len(self.tabTask)+1),0]) #dernier element de la liste (n+1)
        self.cycle = None
        self.finaltabTask = [] #init + tabTask + end
        self.transitive_closure = []
        self.critical_path_tab= [[]]
        self.maximal_critical_path= []
        self.matrix_ordonnacement = []
        self.negval = False

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
        self.build_matrix()

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

    def print_triplet(self): #etape 1
        print(len(self.finaltabTask),"sommets")
        count = 0
        for i in range(len(self.finaltabTask)):
            for j in range(len(self.finaltabTask[i].succesors)):
                print(self.finaltabTask[i].index," -> ",self.finaltabTask[i].succesors[j].index," = ",self.finaltabTask[i].duration)
                count += 1
        print(count,"arcs")

    def build_matrix(self): #etape 2
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
        

        self.matrix_ordonnacement = matrix

    
    def print_matrix(self):
        labels=[i for i in range(len(self.finaltabTask))]
        df = pd.DataFrame(self.matrix_ordonnacement, columns=labels, index=labels)
        print(df)


    def is_cyclic(self,is_print=False):
        cycle = False
        temp_tabtask = copy.deepcopy(self.finaltabTask)
        while(len(temp_tabtask)!=0 and not(cycle)):
            cycle = True # on pas du principe que tant qu'il ne trouve pas d'élément sans successeur cycle = True     
            for i in range(len(temp_tabtask)):
                if len(temp_tabtask[i].predecessors) == 0:
                    cycle = False # s'il trouve un element sans successeur ce n'est pas cyclique
                    for j in range(len(temp_tabtask[i].succesors)):
                        temp_tabtask[i].succesors[j].sup_predecessors(temp_tabtask[i].index) #on supprime l'élément
                    temp_tabtask.pop(i)
                    break #la taille de la liste a changer pour eviter tout erreur on recommence

        # on sait s'il le graphe est cyclique ou non on cherche maintenant quel est le cycle
        if is_print and cycle:
            print("Ce graphe est cyclique")
            if not self.negval:
                print("Ce graphe ne possède pas d'arc négatif.")
            cycle_suc = False
            while(len(temp_tabtask)!=0 and not(cycle_suc)):
                cycle_suc = True # on pas du principe que tant qu'il ne trouve pas d'élément sans successeur cycle = True     
                for i in range(len(temp_tabtask)):
                    if len(temp_tabtask[i].succesors) == 0:
                        cycle_suc = False # s'il trouve un element sans successeur ce n'est pas cyclique
                        for j in range(len(temp_tabtask[i].predecessors)):
                            temp_tabtask[i].predecessors[j].sup_successors(temp_tabtask[i].index) #on supprime l'élément
                        temp_tabtask.pop(i)
                        break #la taille de la liste a changer pour eviter tout erreur on recommence

                # affichage
                for i in temp_tabtask:
                    print(i.index," ->" ,end="")
        elif is_print and (not cycle):
            print("Le graphe n'est pas cyclique")
        return cycle

    def rank(self):
            graph_copy = copy.deepcopy(self)
            self.task_init.rank=0 #Sommet alpha a un rang de 0
            temp = graph_copy.task_init.succesors  # Liste temporaire des taches n'ayant pas de successeurs
            temp_1 = [""]
            cpt = 1 #Les rangs commencent à 1 après alpha
            while (temp_1 != []):
                temp_1 = []
                for i in range(len(temp)):
                    self.finaltabTask[temp[i].index].rank = cpt
                    for j in range(len(temp[i].succesors)):
                        temp[i].succesors[j].sup_predecessors(temp[i].index)
                        if (len(temp[i].succesors[j].predecessors)==0):
                            temp_1.append(temp[i].succesors[j]) #Après suppression de la tâche sans prédécesseurs, on prend ses enfants qui n'ont plus de prédecesseurs pour la prochaine iteration
                temp = temp_1
                cpt+=1

            for i in self.finaltabTask:
                print("La tâche numéro", i.index, "a un rang de ", i.rank)

    def earliest_date(self):#Il faut d'abord définir les rangs des tâches avant de lancer l'ordonnancement
        task_sorted_by_rank = sorted(self.finaltabTask, key=lambda x: x.rank) # On créé une liste qui trie les tâches par ordre croissant de rang
        for i in task_sorted_by_rank:
            if len(i.predecessors)==0:
                i.earliest_date=0
            else:
                temp_earliest_date = [] #Liste temporaire de la date la plus tôt
                for j in i.predecessors:
                    temp_earliest_date.append(j.earliest_date+j.duration) #Pour la date la plus tôt on fait la liste des tâches au plus tôt des prédecesseurs + leur durée
                i.earliest_date = max(temp_earliest_date) #Et on prend le max pour la tâche suivante

        for i in self.finaltabTask:
            print("La tâche numéro", i.index, "a une date minimale de ", i.earliest_date)



    def latest_date(self):#Il faut d'abord définir les rangs et les dates au + tot des tâches avant de lancer cette fonction
        task_sorted_by_rank = sorted(self.finaltabTask, key=lambda x: x.rank, reverse=True)  # On créé une liste qui trie les tâches par ordre décroissant de rang
        for i in task_sorted_by_rank:
            if len(i.succesors) == 0:
                i.latest_date = i.earliest_date #On considère que la date au plus tard du projet est égal à sa date de fin au plus tôt
            else:
                temp_latest_date = []  # Liste temporaire de la date au plus tard
                for j in i.succesors:
                    temp_latest_date.append(j.latest_date - i.duration)  # Pour la date au plus tard on fait la liste des tâches au plus tard des successeurs - la durée de la tache courante
                i.latest_date = min(temp_latest_date)  # Et on prend le min des tâches au plus tard suivantes

        for i in self.finaltabTask:
            print("La tâche numéro", i.index, "a une date maximale de ", i.latest_date)

    def margin(self):#Il faut avoir lancé les fonctions earliest_date et latest_date avant d'exécuter cette fonction
        for i in self.finaltabTask:
            i.margin= i.latest_date-i.earliest_date
            print("La tâche numéro", i.index, "a une marge de ", i.margin)


    def critical_path(self,temp_task=None,temp_critical_path=[]):#Simple squelette, la fonction n'est pas terminé
        if temp_task==None:
            temp_task=self.task_init
            temp_critical_path.append(temp_task.index)
        for i in temp_task.succesors:
            if i.margin==0 and len(i.succesors)>0:
                temp_critical_path.append(i.index)
                self.critical_path(i,copy.deepcopy(temp_critical_path))
                temp_critical_path.pop()
            elif i.margin==0 and len(i.succesors)==0:
                if (i.index==self.task_end.index):
                    temp_critical_path.append(i.index)
                    if(self.critical_path_tab[0]==[]):
                        self.critical_path_tab[0]=temp_critical_path
                    else:
                        self.critical_path_tab.append(copy.deepcopy(temp_critical_path))

    def final_critical_path(self):
        maximal_counter = 0
        for i in range(len(self.critical_path_tab)):
            counter=0
            for j in range(len(self.critical_path_tab[i])-1):
                counter= counter+self.finaltabTask[j].duration
            if counter>maximal_counter:
                maximal_counter=counter
                self.maximal_critical_path=self.critical_path_tab[i]




        
