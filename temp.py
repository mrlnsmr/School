from math import *

Entscheidung = input("Möchten Sie von Grad nach Fahrenheit umrechnen lassen, dann drücken Sie bitte die 1. Möchten Sie von Fahrenheit in Grad umrechnen lassen, dann drücken Sie bitte die 2: ")

if Entscheidung == "1":
    Grad = int(input("Ihre Gradzahl: "))
    Fahrenheit = Grad+32*(9/5)
    print(Fahrenheit)

elif Entscheidung == "2":
    Fahrenheit = int(input("Ihre Zahl: "))
    Grad = (5/9)*(Fahrenheit-32)
    print(Grad)

else: 
    print("Diese Eingabe ist nicht möglich.")