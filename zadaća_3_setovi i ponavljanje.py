import random

brojradnika = 15  # Promjeniti za lakšu provjeru
imer = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
        'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly',
        'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimer = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles',
            'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt',
            'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']
# Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi dostavljanjem.
# Generirati 15 radnika random imena i prezimena iz ponuđene liste, te njegovu satnicu slučajnim
# odabirom floata između 4 i 6 zaokruženu na 2 decimale.

radnici = []
for i in range(brojradnika):
    # Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika
    # {“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
    radnik = {"ime": imer[random.randint(0, (len(imer) - 1))],
              "prezime": prezimer[random.randint(0, (len(prezimer) - 1))],
              "satnica": round(random.uniform(4, 6), 2)}
    radnici.append(radnik)

# Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati”
# #koji generira cijeli broj odrađenih sati u 1 tjednu od 20 do 30.
a = 0
while a < brojradnika:
    radnici[a]["tjedni_sati"] = random.randint(20, 30)
    a += 1
placanja = []
# Nakon toga napraviti obračun množenjem satnice sa tjednim satima
for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    satnica = radnik["satnica"]
    tjedni_sati = radnik["tjedni_sati"]
    isplata = round(satnica * tjedni_sati, 2)
    # rezultate spremiti u listu tuple-a (trojki) oblika (ime, prezime, isplata).
    placanja.append((ime, prezime, isplata))

# Iteriranjem ispisati podatke
for radnik in radnici:
    print(radnik)
for ime, prezime, isplata in placanja:
    print(ime, prezime, isplata)
# zatim izračunati ukupnu i prosječnu isplatu za taj tjedan.
ukupno_isplata = 0
for _, _, isplata in placanja:
    ukupno_isplata += isplata
ukupno_isplata = round(ukupno_isplata, 2)  # zaokruživanje jer se stvara problem
prosjecna_isplata = round(ukupno_isplata / len(placanja), 2)
print("Prosječna zarada radnika je u tjednu: ", prosjecna_isplata, "KM,")
print("a ukupna zarada radnika u ovome tjednu je: ", ukupno_isplata, "KM")
# Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.
print("Iznadprosječno su zaradili")
for ime, prezime, isplata in placanja:
    if isplata >= prosjecna_isplata:
        print(f"{ime} {prezime}")
