from math import *

print("Hallo, ich werde Ihnen den Flächeninhalt Ihres Dreiecks ausrechnen.")
print("")

a = int(input("Wie lang ist die Seite a?"))
b = int(input("Wie lang ist die Seite b?"))
c = int(input("Wie lang ist die Seite c?"))

if a+b<c or a+c<b or b+c<a:
    print("Mit diesen Längen würde kein Dreieck entstehen.")

else:
    s = (a+b+c)/2
    A = (sqrt(s*(s-a)*(s-b)*(s-c)))

    print("Flächeninhalt =", A)

