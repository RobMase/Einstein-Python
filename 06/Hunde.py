class Hund:
    def __init__(self, name, bellGeraeusch, alter, fellFarbe):
        self.bellLaut = bellGeraeusch
        self.alter = alter
        self.fellFarbe = fellFarbe
        self.name = name

    def gibPfote(self):
        print(f"Hallo! ich bin {self.name}")
        print("Ich geb dir die Pfote.")

    def bellen(self):
        print(self.bellLaut)

    def sitz(self):
        print(" Ich sitze :-)  ")

bello = Hund("Bello", "Wau wau!", 3, "gruen")
bello.bellen()
bello.gibPfote()

leika = Hund("Leika", "Kleff kleff!", 0.3, "schwarz")
leika.bellen()
leika.gibPfote()