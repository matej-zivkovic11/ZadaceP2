import re

def provjeri_lozinku(lozinka):
    # Provjera velikog slova, malog slova, broja, rečeničnog znaka
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.,?!@#$%^&*()-_+=]).+$"
    return re.match(regex, lozinka)

def ima_8_znakova(lozinka):
    # Provjera duljine
    if len(lozinka)>=8:
        return True
    else:
        return False

print("Unesite lozinku koja sadrži veliko i malo slovo, broj i rečenični znak *[.,?!@#$%^&*()-_+=]: ")
while 1:
    
    lozinka0 = str(input())
    
    if provjeri_lozinku(lozinka0) and ima_8_znakova(lozinka0):
        print("Jaka lozinka.")
        print("Potvrdite lozinku:")
        lozinka1=str(input())
        if lozinka0 == lozinka1:
            print("Uspješno ste potvrdili lozinu")
            break
    else:
        print("Slaba lozinka, pokušajte ponovo ")
