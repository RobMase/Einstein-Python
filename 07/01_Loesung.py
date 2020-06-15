import random

class Wuerfel:
    def wuerfeln(self):
        print(random.randint(1, 6))

class Spiel:
    def __init__(self, anzahl_wuerfel):
        self.alleWuerfel = []
        for index in range(anzahl_wuerfel):
            self.alleWuerfel.append(Wuerfel())

    def wuerfelAlle(self):
        for wuerfel in self.alleWuerfel:
            wuerfel.wuerfeln()

game = Spiel(3)
game.wuerfelAlle()