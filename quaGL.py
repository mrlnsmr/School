from math import *

a = int(input("Bitte geben Sie a ein: "))
b = int(input("Bitte geben Sie b ein: "))
c = int(input("Bitte geben Sie c ein: "))

if a == 0:
    x = -b/c
    
elif a == 0 and b == 0:
    x = c
    
else:
    b = b/a
    c = c/a
    dis = (b/2)*(b/2)-c
    if dis < 0 :
        print("Es sind keine Nullstellen vorhanden")
    elif dis == 0:
        x = -b/2
        print("Die Nullstelle ist: x = ", x)
    else:
        x1 = -b/2 + dis
        x2 = -b/2 - dis

print("Die Nullstellen sind: x1 = ", x1)
print("                      x2 = ", x2)