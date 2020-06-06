class ersteKlasse:
    pass


class Irgendwas:
    klassenVariable = 0

    def __init__(self):
        self.instanzVariable = 10

    def meineFunktion(self):
        return "Hallo Klassen-Welt"


instanzObjekt = Irgendwas()
x = Irgendwas()
y = Irgendwas()

print(instanzObjekt.meineFunktion())
print(instanzObjekt.instanzVariable)
print(instanzObjekt.klassenVariable)

# print(instanzObjekt.klassenVariable)
# print(instanzObjekt.instanzVariable)
# print(instanzObjekt.meineFunktion())

# methodenObjekt = instanzObjekt.meineFunktion
# print(methodenObjekt())