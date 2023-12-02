from math import *

x = input("Gebe einen Wert für x ein: ")
y = input("Gebe einen Wert für y ein (er muss sich von x unterscheiden): ")

if x == y:
    print("x und y müssen sich unterscheiden!")

else:
    hv = x
    x = y
    y = hv
    print("x=", x, "y=", y)
    
#Die Variable hv ist nötig, da man x zwischenspeichern muss, damit es nicht verloren geht, wenn man dann den Wert von x mit dem Wert von y überschreibt.