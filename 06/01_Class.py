class ersteKlasse:
    pass

class KlassenName:
    klassenVariable = 0

    def __init__(self):
        self.instanzVariable = 10

    def meineFunktion(self):
        return "Hallo Klasen-Welt"

instanzObjekt = KlassenName()
print(instanzObjekt.klassenVariable)
print(instanzObjekt.instanzVariable)
print(instanzObjekt.meineFunktion())

methodenObjekt = instanzObjekt.meineFunktion
print(methodenObjekt())


def funktion(printstring):
    print(printstring)

funktion("hez hez")