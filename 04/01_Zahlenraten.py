import random
minNum = 0
maxNum = 10
geraten = 0
richtigGeraten = 0

while True:
    gesucht = random.randrange(minNum, maxNum)
    value = input(f"Gesucht ist eine Zahl zwischen {minNum} bis {maxNum}, gebe exit ein um das spiel zu beenden: ")
    geraten += 1
    if value == "exit":
        break # beenden
    elif gesucht == int(value):
        print("Du hast richtig geraten")
        richtigGeraten += 1
    else:
        print(f"Du hast leider falsch geraten {gesucht} wäre richtig gewesen")

print(f"Danke fürs spielen du hast insgesamt {geraten} mal geraten, davon lagst du {richtigGeraten} mal richtig ({((richtigGeraten / float(geraten)) * 100):.2f}%)")