def pozdrav_ime(ime):
    return f"Pozdrav {ime}!"

dobrodosao_ime = lambda ime: f"Dobrodošao {ime}!"

def pozovi_funkciju(funkcija, ime):
    return funkcija(ime)

moje_ime = "Matej"

poruka1 = pozovi_funkciju(pozdrav_ime, moje_ime)
print(poruka1)

poruka2 = pozovi_funkciju(dobrodosao_ime, moje_ime)
print(poruka2)