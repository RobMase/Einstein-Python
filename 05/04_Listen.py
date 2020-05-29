namen_liste = ["Robert", "Florian", "Johny"]

print(f"Eine List von Namen: {namen_liste}")

print(f"Eine List von Zahlen: { [1,2,3,4,-100] }")
print(f"Eine sehr gemischte Liste: { [1,'a', True] }")

erste_liste = [1,2,3]
zweite_liste = [4,5,6]
print(f"Listen kann man anhängen: {erste_liste + zweite_liste}")

print(f"Das erste Element der Namensliste: {namen_liste[1]}")
print(f"Das wirklich erste Element der Namensliste: {namen_liste[0]}")

namen_liste.append("Hannah")
print(f"Die neue Namensliste: {namen_liste}")

pop = namen_liste.pop()
print(f"Pop: {pop}")
print(f"Die aktuelle Namensliste: {namen_liste}")

print(f"Florian steht an {namen_liste.index('Florian')}. Stelle ")

namen_liste.remove("Florian")
print(f"Florian steht an {namen_liste.index('Florian')}. Stelle ")