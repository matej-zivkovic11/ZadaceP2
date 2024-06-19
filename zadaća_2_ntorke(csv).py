from csv import reader

# Učitavanje podataka iz CSV datoteke
putanja_datoteke = 'rezultati.csv'
studenti = []

with open(putanja_datoteke, 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)  # preskoči zaglavlje
    for redak in csv_reader:
        # Filtriranje i prilagođavanje redaka koji imaju više ili manje od tri elementa
        if len(redak) >= 3 and redak[2].isdigit():  # Provjera da bodovi nisu prazni i da su numerički
            ime, prezime, bodovi = redak[0], redak[1], int(redak[2])
            studenti.append((ime, prezime, bodovi))

# Filtriranje studenata koji su položili ispit (bodovi > 49)
polozeni_studenti = [student for student in studenti if student[2] > 49]

# Ispis studenata koji su položili ispit
print("Studenti koji su položili ispit:")
for student in polozeni_studenti:
    print(student)

# Sortiranje liste po prezimenima
sortirani_studenti = sorted(polozeni_studenti, key=lambda student: student[1])

# Ispis sortiranih studenata po prezimenima
print("\nSortirani studenti po prezimenima:")
for student in sortirani_studenti:
    print(student)

# Kreiranje rječnika s brojem ostvarenih ocjena po bodovnim rangovima
ocjene_rjecnik = {}
for student in sortirani_studenti:
    bodovi = student[2]
    if bodovi >= 90:
        ocjena = 5
    elif bodovi >= 75:
        ocjena = 4
    elif bodovi >= 60:
        ocjena = 3
    elif bodovi >= 50:
        ocjena = 2
    else:
        ocjena = 1  # Ne bi trebao biti u ovoj listi jer smo filtrirali položene studente
    
    if ocjena in ocjene_rjecnik:
        ocjene_rjecnik[ocjena] += 1
    else:
        ocjene_rjecnik[ocjena] = 1

# Ispis broja ostvarenih ocjena po bodovnim rangovima
print("\nBroj ostvarenih ocjena po bodovnim rangovima:")
for ocjena, broj in ocjene_rjecnik.items():
    print(f"Ocjena {ocjena}: {broj} studenata")