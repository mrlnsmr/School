from math import *

x = int(input("Bitte geben Sie einen Wert für x ein: "))
y = int(input("Bitte geben Sie einen Wert für y ein: "))
        
while y > 0:
    r = x % y
    x = y
    y = r
    
print("ggT:",x)
        