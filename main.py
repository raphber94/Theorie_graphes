from functions import *
tableau = read_file("test.txt")
for ligne in tableau:
    print(ligne)
### initialisation graph ###
tabTask = build_class(tableau)
graph = Graph(tabTask)
graph.build_predecessors(tableau)
graph.build_succesors(tableau)
graph.build_init()

### TEST ###
for i in range(len(graph.task_init.succesors)):
    print(graph.task_init.succesors[i].index)
for i in range(len(tabTask)):
    #print(tabTask[i].index)
    print("pour ",i+1)
    for task in tabTask[i].predecessors:
        print(task.index)
    print("\n")

#G = build_graph(tableau)



#calendrier(tableau)