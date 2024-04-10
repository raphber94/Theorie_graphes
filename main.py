from functions import *
import pandas as pd
import numpy




tableau = read_file("test.txt")
for ligne in tableau:
    print(ligne)
### initialisation graph ###
tabTask = build_class(tableau)
graph = Graph(tabTask)
graph.initialisation(tableau)

### Print 
graph.print_triplet()
graph.print_matrix()
