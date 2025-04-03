# Aplikacija za adresar

## Opis zadatka

**Cilj zadatka**: Izraditi aplikaciju koja omogućuje pohranu i upravljanje podacima o kontaktima u adresaru. Podaci će biti pohranjeni u JSON formatu, a aplikacija će pružati opcije za dodavanje, pretragu, prikazivanje, brisanje kontakata te provjeru ispravnosti unosa.

## Detaljan opis funkcionalnosti

Aplikacija za adresar treba omogućiti sljedeće funkcije:

1. **Dodavanje kontakta**: 
   - Korisnik treba moći unijeti ime, broj telefona, e-mail i adresu kontakta.
   - Ime treba biti samo tekstualni string (ne smije biti prazno).
   - Telefon treba sadržavati samo brojke (provjera da telefon ne sadrži nikakve druge znakove).
   - E-mail treba sadržavati znak `@` (osnovna provjera valjanosti).
   - Ovi podaci moraju biti pohranjeni u JSON datoteku tako da budu trajno dostupni.

2. **Prikazivanje svih kontakata**: 
   - Prikazivanje svih pohranjenih kontakata, uključujući ime, broj telefona, e-mail i adresu.
   - Ako adresar ne sadrži nikakve kontakte, aplikacija treba ispisati poruku da je adresar prazan.

3. **Pretraga kontakta**: 
   - Omogućiti korisniku da pretraži adresar prema imenu kontakta.
   - Ako kontakt nije pronađen, aplikacija treba ispisati odgovarajuću poruku.

4. **Brisanje kontakta**: 
   - Omogućiti brisanje kontakta iz adresara prema imenu.
   - Ako kontakt nije pronađen, aplikacija treba ispisati odgovarajuću poruku.

5. **Spremanje i učitavanje podataka**: 
   - Svi podaci (kontakti) trebaju biti pohranjeni u JSON datoteku.
   - Aplikacija mora omogućiti učitavanje podataka iz datoteke pri pokretanju i spremanje ažuriranih podataka nakon svakog unosa, brisanja ili promjene.

6. **Glavni izbornik**: 
   - Korisnik će imati mogućnost odabrati jednu od opcija putem broja u glavnom izborniku (dodavanje, prikazivanje, pretraga, brisanje ili izlaz).
   - Izbornik mora biti jednostavan i intuitivan, omogućujući korisniku da lako navigira između opcija.

## Kako koristiti aplikaciju

1. Pokrenite aplikaciju tako da pokrenete Python skriptu.
2. Odaberite jednu od opcija iz glavnog izbornika:
   - 1 za dodavanje kontakta
   - 2 za prikazivanje svih kontakata
   - 3 za pretragu kontakta prema imenu
   - 4 za brisanje kontakta prema imenu
   - 5 za izlaz iz aplikacije
3. Za unos kontakta, unesite ime, broj telefona, e-mail i adresu. Provjere će osigurati da su podaci ispravni.
4. Kontakti će biti pohranjeni u `adresar.json` datoteku.

## Podaci u JSON formatu

Kontakti će biti pohranjeni u JSON formatu sličnom ovom primjeru:

```json
{
    "Kontakti": {
        "John Doe": {
            "Telefon": "123456789",
            "Email": "johndoe@example.com",
            "Adresa": "123 Main St"
        },
        "Jane Smith": {
            "Telefon": "987654321",
            "Email": "janesmith@example.com",
            "Adresa": "456 Elm St"
        }
    }
}
