import random

minimaleZahl = 0
maximaleZahl = 10
richtigGeraten = 0
insgesamtGeraten = 0

while True:
    eingabe = input(f"Gebe eine Zahl zwischen {minimaleZahl} - {maximaleZahl} ein oder exit um das spiel zu beenden: ")
    erwartet = random.randint(minimaleZahl, maximaleZahl - 1)
    if eingabe == "exit":
        break
    elif int(eingabe) == erwartet:   
        richtigGeraten += 1 # richtigGerate = richtigGeraten + 1
        print("Du hast richtig geraten")
    else:
        print(f"Du hast falsch geraten, richtig wäre {erwartet} gewesen")
    insgesamtGeraten += 1 
    
if insgesamtGeraten == 0:
    print("Du hast gar nicht gespielt, versuch es doch einmal :(")
else:
    prozent = (float(richtigGeraten) / insgesamtGeraten) * 100
    print(f"Danke dass du das Spiel gespielt hast, du hast insgesamt {insgesamtGeraten} davon {richtigGeraten} mal richtig ({prozent:.2f}%)")