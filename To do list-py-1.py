ToDoList = []
nombreTache = 5
for i in range(1, nombreTache+1):
    tache = input("Entrez une tache:")
    ToDoList.append(tache)
print("--- To Do List initial ---")
print(ToDoList)
taille = len(ToDoList)
for index, name in enumerate(ToDoList):
    print(f"{index}: {name}")
supTache = input("Quelle tache voulez-vous supprimer ?")
if supTache in ToDoList:
    ToDoList.remove(supTache)
else:
     print("Cette tache n'existe pas")
print("--- To Do List suppression ---")
print(ToDoList)
print("--- To Do List modification ---")
oui, non = "oui", "non"
qTache = input("Aimeriez-vous modifiez une tache ?")
if qTache == oui:
    rempTache = input("Donnez cette tache:")
    index = int(input("Donne l'index de la tache: "))
    ToDoList[index] = rempTache
    print(ToDoList)
if qTache == non:
    print("A la prochaine")
print("Merci a la prochaine")