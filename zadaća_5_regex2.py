import re

def email_validacija(email):
    
    #Napisati regex za provjeru validnosti unosa e-maila.
    #E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
    
    re_email = r"^\w+\.+\w+@fpmoz\.sum\.ba$"
    if re.match(re_email, email):
        print("email je validan.")
    else:
        print("email nije validan.")

def edu_id_validacija(edu):
    
    #Napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba
    #Gdje je i prvo slovo imena + prezime.
    #X predstavlja bilo koji broj (moze ici u beskonacnost),
    #a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
    
    re_edu = r"^[a-z]+\w+[0-9]*@sum\.ba$"#^[a-z]+\w...$ je istovjetno ^\w...$ 
    if re.match(re_edu, edu):
        print("eduid je validan.")
    else:
        print("eduid nije validan.")

        
print("Primjer: ime.prezime@fpmoz.sum.ba unesite vaš email: ")
email=str(input())
email_validacija(email)

print("Primjer: iprezimeX@sum.ba i-prvo slovo imena X-cijeli broj, unesite vaš eduid: ")
eduid=str(input())
edu_id_validacija(eduid)
