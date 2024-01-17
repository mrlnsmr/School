from math import *

liste = []

liste=list(map(int(input("Bitte eine Liste natürlicher Zahlen eingeben").split())))

print(liste)

listeSortiert = []
listeUnsortiert = liste

while listeUnsortiert != []:
    kleinsterWert = min(listeUnsortiert)
    Position = listeUnsortiert.index(kleinsterWert)
    listeSortiert.append(kleinsterWert)
    listeUnsortiert.remove(kleinsterWert)

print(listeSortiert) 