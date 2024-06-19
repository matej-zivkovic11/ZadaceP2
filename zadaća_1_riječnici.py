import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
         'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
         'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
         'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
         'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

brojac_imena = {}
for ime in imena:
    if ime in brojac_imena:
        brojac_imena[ime] += 1
    else:
        brojac_imena[ime] = 1

print("Brojanje imena:")
for ime, broj in brojac_imena.items():
    print(f"{ime}: {broj}")

ocjene = {ime: random.randint(1, 5) for ime in imena}

brojac_ocjena = {}
for ocjena in ocjene.values():
    if ocjena in brojac_ocjena:
        brojac_ocjena[ocjena] += 1
    else:
        brojac_ocjena[ocjena] = 1

print("\nBrojanje ocjena:")
for ocjena, broj in brojac_ocjena.items():
    print(f"Ocjena {ocjena}: {broj}")

broj_prolaznih = sum(broj for ocjena, broj in brojac_ocjena.items() if ocjena > 1)
ukupno_ocjena = len(imena)
postotak_prolaznosti = (broj_prolaznih / ukupno_ocjena) * 100

print(f"\nPostotak prolaznosti: {postotak_prolaznosti:.2f}%")