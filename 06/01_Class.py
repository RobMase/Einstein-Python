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

# print(instanzObjekt.meineFunktion())
# print(f"Instanzvariable: {instanzObjekt.instanzVariable}")
# print(f"Klassenvariable: {instanzObjekt.klassenVariable}")


class Irgendwas2:
    klassenVariable = 1

    def __init__(self, instanzvariable):
        self.instanzVariable = instanzvariable

    def meineFunktion(self):
        return "Hallo Klassen-Welt"

instanzObjekt2 = Irgendwas2(10)
instanzObjekt3 = Irgendwas2(20)
instanzObjekt2.klassenVariable = 100
print(f"instanzObjekt2 von Klasse Irgendwas2: {instanzObjekt2.klassenVariable}")
print(f"instanzObjekt3 von Klasse Irgendwas2: {instanzObjekt3.klassenVariable}")

# methodenObjekt = instanzObjekt.meineFunktion
# print(methodenObjekt())