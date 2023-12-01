from math import *

Kennzeichen = input("Bitte gib dein Kennzeichen ein (E = Erwachsender), (K = Kind), (R = Rentner), (S =Schüler/Student): ")
n = int(input("Wie viele Hallen hast du besucht?"))

if Kennzeichen == "E":
    if n < 3:
        P = 3
        print("Der Eintrittspreis kostet", P, "€")
    else:
        P = 3*0.75
        print("Der Eintrittspreis kostet", P, "€")


elif Kennzeichen == "K":
    if n < 3:
        P = 1.5
        print("Der Eintrittspreis kostet", P, "€")
    else:
        P = 1.5*0.75
        print("Der Eintrittspreis kostet", P, "€")

elif Kennzeichen == "R":
    if n < 3:
        P = 2
        print("Der Eintrittspreis kostet", P, "€")
    else:
        P = 2*0.75
        print("Der Eintrittspreis kostet", P, "€")

elif Kennzeichen == "S":
    if n < 3:
        P = 2
        print("Der Eintrittspreis kostet", P, "€")
    else:
        P = 2*0.75
        print("Der Eintrittspreis kostet", P, "€")

else:
    print("Das ist kein gültiges Kennzeichen.")