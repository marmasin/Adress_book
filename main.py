import json

DATOTEKA_ADRESARA = "adresar.json"

def ucitaj_podatke() -> dict:
    try:
        with open(DATOTEKA_ADRESARA, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    """
    Učitava podatke iz JSON datoteke. Ako datoteka ne postoji ili je oštećena, vraća prazan adresar.

    Returns:
        dict: Podaci o kontaktima iz JSON datoteke ili prazan adresar.
    """

def spremi_podatke(podaci: dict) -> None:
    with open(DATOTEKA_ADRESARA, "w", encoding="utf-8") as file:
        json.dump(podaci, file, indent=4, ensure_ascii=False)
   
    """
    Spremi podatke u JSON datoteku.

    Args:
        podaci (dict): Podaci koji će biti pohranjeni u datoteku.
    """


def provjeri_telefon(telefon: str) -> bool:
    return telefon.isdigit()    
    """
    Provjerava je li telefon sastavljen samo od brojki.

    Args:
        telefon (str): Broj telefona.

    Returns:
        bool: True ako telefon sadrži samo brojke, inače False.
    """


def provjeri_email(email: str) -> bool:
    return "@" in email
    """
    Provjerava sadrži li email znak '@'.

    Args:
        email (str): Email adresa.

    Returns:
        bool: True ako email sadrži '@', inače False.
    """
 

def dodaj_kontakt(Ime: str, Telefon: str, Email: str, Adresa: str) -> None:
    kontakti = ucitaj_podatke()
    if not provjeri_telefon(Telefon) or not provjeri_email(Email):
        print("Neispravan format telefona ili emaila.")
        return
    if not kontakti:
        kontakti = {}
    if Ime not in kontakti:
        kontakti[Ime] = {"telefon": Telefon, "email": Email, "adresa": Adresa}
    spremi_podatke(kontakti)
    print("Kontakt uspješno dodan.")
    """
    Dodaje kontakt u adresar ako su svi podaci ispravni.

    Args:
        ime (str): Ime kontakta.
        telefon (str): Telefon kontakta.
        email (str): Email kontakta.
        adresa (str): Adresa kontakta.
    """

def prikazi_kontakte() -> None:
    kontakti = ucitaj_podatke()
    if not kontakti:
        print("Adresar je prazan.")
        return
    for ime, kontakt in kontakti.items():
        print(f"Ime: {ime}, Telefon: {kontakt['telefon']}, Email: {kontakt['email']}, Adresa: {kontakt['adresa']}")
     
    """
    Prikazuje sve kontakte u adresaru.
    """

def pretrazi_kontakt(ime: str) -> None:
    kontakti = ucitaj_podatke()
    if ime in kontakti:
        kontakt = kontakti[ime]
        print(f"Ime: {ime}, Telefon: {kontakt['telefon']}, Email: {kontakt['email']}, Adresa: {kontakt['adresa']}")
    else:
        print("Kontakt nije pronađen.")
    
    """
    Pretražuje adresar prema imenu kontakta.

    Args:
        ime (str): Ime kontakta za pretragu.
    """


def obrisi_kontakt(ime: str) -> None:
    kontakti = ucitaj_podatke()
    ime_za_brisanje = ime
    if ime_za_brisanje in kontakti:
        del kontakti[ime_za_brisanje]
        spremi_podatke(kontakti)
        print("Kontakt uspješno obrisan.")
    else:
        print(f"Kontakt s imenom {ime_za_brisanje} nije pronađen.")
    
    
    """
    Briše kontakt iz adresara prema imenu.

    Args:
        ime (str): Ime kontakta koji će biti obrisan.
    """

def main() -> None:
    """
    Glavna funkcija koja omogućava korisniku da bira opcije u adresaru.
    """
    while True:
        print("\nAdresar - Odaberite opciju:")
        print("1. Dodaj kontakt")
        print("2. Prikaži sve kontakte")
        print("3. Pretraži kontakt")
        print("4. Obriši kontakt")
        print("5. Izlaz")
        
        izbor = input("Unesite broj opcije: ")
        if izbor == "1":
            ime = input("Unesite ime: ")
            telefon = input("Unesite broj telefona: ")
            email = input("Unesite email: ")
            adresa = input("Unesite adresu: ")
            dodaj_kontakt(ime, telefon, email, adresa)
        elif izbor == "2":
            prikazi_kontakte()
        elif izbor == "3":
            ime = input("Unesite ime za pretragu: ")
            pretrazi_kontakt(ime)
        elif izbor == "4":
            ime = input("Unesite ime za brisanje: ")
            obrisi_kontakt(ime)
        elif izbor == "5":
            print("Izlaz iz aplikacije.")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()
