class Hund:
    def __init__(self, belllaut):
        self.bellLaut = belllaut

    def bellen(self):
        print(self.bellLaut)

###################

class Bernhardiner(Hund):
    def __init__(self):
        self.bellLaut = "Wau wau wau!"

###################

class Schaeferhund(Hund):
    def __init__(self):
        self.bellLaut = "Wau wau Kleff!"

###################

fiffi = Bernhardiner()
fiffi.bellen()

koeter = Schaeferhund()
koeter.bellen()

class Bernersennenhund(Hund):
    def __init__(self, belllaut):
        self.bellLaut = belllaut

bello = Bernersennenhund("Bell bell")
bello2 = Bernersennenhund("Bello bello")

# hundeList = [fiffi, koeter]
# print(f"List von Hunden: {hundeList}")

bello.bellen()
bello2.bellen()

# print(f"bello: {bello.bellen()}")
# print(f"bello2: {bello2.bellen()}")