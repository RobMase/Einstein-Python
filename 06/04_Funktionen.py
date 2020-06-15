def funktionenName(vorname = "StandardVorname", nachname = "StandardNachname"):
    kompletterName = vorname + " " + nachname
    print(f"Hallo {kompletterName}")

funktionenName()
funktionenName("Robert")
funktionenName("Robert", "Masur")

def funktionenNameGehtNicht(vorname , nachname = "asnndkasd"):
    kompletterName = vorname + " " + nachname
    print(f"Hallo {kompletterName}")