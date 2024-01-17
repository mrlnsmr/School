#Variablen
y=0
Beweise = 0
wichtigerBeweis = False
Code = False
Stichwunde = False
Messer = False

#Einführung
print("Du bist Mordkommisar/in und kommst Donnerstag Morgen in dein Büro und bekommst einen neuen Fall auf den Tisch gelegt. Du liest dir die Akten durch und trinkst den ersten Kaffee des Morgens. Eine Kollegin erzählt dir vom Praktikanten namens Tom und fragt, ob er dich in deinem neuen Fall unterstützen könnte. Du überlegst ob er nützlich sein könnte oder dir eher zur Last fällt und triffst eine Entscheidung.")

#Partner
e1 = input("Möchtest du den Praktikanten mitnehmen? --> ja / nein : ")
if e1 == "ja":
    Partner = True
    print("Du entscheidest dich den Praktikanten aufzunehmen und erklärst ihm deinen Fall. Er hört dir gespannt zu und scheint dir später vielleicht noch nützlich zu sein.")

else:
    Partner = False
    print("Du hast absolut keine Lust einen Praktikanten mitzuschleppen und schickst ihn ins Archiv, wo er nach einer Akte suchen soll, die du letzte Woche schon in den Müll geworfen hast. Den siehst du nicht so schnell wieder.")

x=0
print("Nachdem du dir die Akte nochmal genauer angeschaut hast weißt du, dass die Leiche Tatjana heißt und hast 4 To-Do´s festgestellt, die du erledigen kannst: Leiche untersuchen, Tatort erkunden, Zeugen befragen oder Verdächtige befragen.")
#Entscheidung 2 (4x)
while x < 4:
    e2 = input("Was möchtest du tun? (Du kannst jede Aktivität nur einmal tun!)")

    if e2 == "Leiche untersuchen":
        x = x+1
        print("Du checkst nochmal die Nummer für den Leichenraum und merkst dabei, dass die letzte Nummer nicht lesbar ist. Genervt begibst du in die unterste Etage bis du vor den zwei möglichen Türen stehst hinter denen sich die Leiche befinden kann.")
        
        #Entscheidung 3
        e3 = input("Welche Tür wählst du? --> links / rechts : ")
        if e3 == "links":
            print("Hurra! Du hast die richtige Tür gewählt und siehst die Leiche auf einem Tisch liegen. Das erste was dir auffällt, als du dich zum Tisch begibst, sind die Stichwunden im Bauch (Hinweise: +1).")
            Stichwunde = True
            Beweise = 1

            #Entscheidung 4
            e4 = input("Möchtest du die Leiche noch weiter untersuchen? --> ja / nein : ")
            if e4 == ja:
                print("Du entscheidest dich die Leiche weiter zu untersuchen und findest in der rechten Hand einen Zettel mit einer Zahlenfolge, die aussieht wie ein Code: 5381")
                Code = True
        else:
            print("Oh man! Du merkst, dass du die falsche Tür gewählt hast und eine komplett andere Leiche auf dem Tisch liegt. Plötzlich wirst du von deiner Kollegin angerufen, dass du ganz schnell wieder nach oben musst. Als du dort ankommst scheint nichts ungewöhnlich zu sein und dir wird gesagt, dass es nur ein Fehlalarm war. Die Leichenräume sind jetzt leider für dich verschlossen.")

    elif e2 == "Tatort erkunden":
        x = x+1
        print("Du fährst zum Tatort und wirst direkt von der Polizei, die alles abgesperrt hat, durchgelassen und beginnst deine Erkundung. Als erstes gehst du in die Küche, wo der Mord begangen worden ist. Du gehst um den Tisch herum und siehst ein Messer mit Blut an der Klinge auf dem Boden liegen. Die Mordwaffe (Hinweise: +1). ")
        if Stichwunde == True:
            print("Du erinnerst dich an die Stichwunden, die du an der Leiche gesehen hast und verknüpfst diese mit der Mordwaffe.")
        else:
            print("Nachdem du dich noch gründlich in der Küche umgesehen hast gehst du weiter und gehst in die obere Etage. Auf einmal hörst du ein Knurren hinter dir und drehst dich langsam um. Vor dir steht eine riesige Bulldogge, die nicht sehr freundlich zu sein scheint.")
            if Partner == True:
                print("Der Praktikant, der die ganze Zeit direkt hinter dir war stellt sich auf einmal vor dich und geht langsam auf die Bulldogge zu. Er kniet sich vor ihr hin und beginnt sie zu streicheln. Da erinnerst du dich, dass deine Kollegin erzählt hat, dass er sehr gut mit Tieren umgehen kann und spürst Erleichterung in deinem Körper. Der Praktikant und die Bulldogge scheinen sich angefreundet zu haben, denn auf einmal springt die Bulldogge im Kreis als würde sie euch etwas zeigen wollen. Ihr folgt ihr in ein Schlafzimmer bis sie vor einer Schranktür stehen bleibt. Du öffnest die Tür langsam und ihr entdeckt einen Tresor.")
                if Code == True:
                    print("Du erinnerst dich an die Zahlenfolge auf dem Zettel und gibst ihn ein. Die Tür des Tresors springt auf und du findest ein Testament, welches dem Opfer gehört.")
                else:
                    print("Da du leider kein Wissen über den Code hast kannst du den Tresor nicht öffnen und verlässt das Haus.")
            else:
                print("Da du nie was mit Tieren am Hut hattest weißt du nicht wie du dich verhalten sollst. Du hast zwei Möglichkeiten: Vorbeigehen oder Verschwinden")
                #Entscheidung 5
                e5 = input("Was tust du? ")
                if e5 == "Vorbeigehen":
                    print("Du versuchst an der Bulldogge vorbeizugehen, doch sie springt dich an und beißt dir ins Bein. Durch den Schreck wird dir schwarz vor Augen. Später wachst du im Krankenhaus auf und erfährst, dass der Fall an jemand anderen übergeben wurde.")
                    print("ENDE")
                else:
                    print("Du entscheidest dich zu Verschwinden und fährst wieder zurück ins Büro.")

    elif e2 == "Zeugen befragen":
        x = x+1

    elif e2 == "Verdächtige befragen":
        x = x+1

    else:
        print("Du entscheidest dich nichts zu tun und nimmst den Rest des Tages frei. Irgendwer anders wird sich schon um den Fall kümmern.")
        print("ENDE")
        y=1
        x=x+4


if y != 1:
    if Beweise <= 2:
        print("keiner wird verhaftet")

    elif Beweise >= 2 and Beweise < 6:
        if wichtigerBeweis == True:
            print("Torsten wird verhaftet, da er den Mord begangen hat.")
            print("ENDE")

        else:
            print("Tjorben wird verhaftet, weil er beim Mord geholfen hat. Leider konntest du den Mörder nicht identifizieren.")
            print("ENDE")

    else:
        print("Torsten und Tjorben werden beide verhaftet.")
        print("ENDE")


else:
    exit()
