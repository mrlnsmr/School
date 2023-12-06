from math import *

liste = []

Eingabe = int(input("Geben Sie Zahlen für die Liste oder Q zum Beenden Ihrer Eingabe ein: "))

while Eingabe != "Q":
    liste.append(Eingabe)
    Eingabe = int(input("Geben Sie Zahlen für die Liste oder Q zum Beenden Ihrer Eingabe ein: "))

listeSortiert = []
listeUnsortiert = liste

while listeUnsortiert != []:
    kleinsterWert = min(listeUnsortiert)
    Position = listeUnsortiert.index(kleinsterWert)
    listeSortiert.append(kleinsterWert)
    listeUnsortiert.remove(kleinsterWert)

print(listeSortiert) 