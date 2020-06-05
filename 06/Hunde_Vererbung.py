class Hund:
    def __init__(self):
        self.bellLaut

    def bellen(self):
        print(self.bellLaut)

class Bernhardiner(Hund):
    def __init__(self):
        self.bellLaut = "Wau wau wau!"

fiffi = Bernhardiner()
fiffi.bellen()