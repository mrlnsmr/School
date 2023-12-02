from math import *

print("Hallo, ich werde Ihnen den Flächeninhalt Ihres Dreiecks ausrechnen.")
print("")

a = map(int,input("Wie lang ist die Seite a? "))
b = map(int,input("Wie lang ist die Seite b? "))
c = map(int,input("Wie lang ist die Seite c? "))

s = (a+b+c)/2
A = (sqrt(s*(s-a)*(s-b)*(s-c)))

print("Flächeninhalt = ", A)