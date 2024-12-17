import os

def meniu():
    print(
    """
    Alegeti din urmatoarele comenzi
    1. Adauga pachet
    2. Modifica pretul unui pachet
    3. Stergerea tuturor pachetelor de calatorie disponibile pentru o destinatie
    4. Stergea toate pachetelor de calatorie care au o durata mai mica decat nr de zile dat
    5. Stergerea tuturor pachetelor de calatorie care au pretul mai mare decat o suma data
    6. Afisarea listei cu pachetele de calatorie dintr-un interval dorit
    7. Afiseaza pachetele cu o destinatie data si cu un pret mai mic decat parametrul suma
    8. Afiseaza pachetele care au o anumita data de sfarsit
    9. Afiseaza numarul de pachete de calatorie care au o destinatie data
    10. Afiseaza destinatia, perioada si pretul pachetelor de calatorie dintr-un interval dat
    11. Afiseaza media de pret a unei destinatii dorite
    12. Afiseaza pachetele de calatorie cu un pret mai mic sau egal
        sau au o detinatie identica cu cea data ca parametru
    13. Afiseaza pachetele de calatorie care contin zile dintr-o
        luna data ca parametru
    14. Undo 
    """
    )

def curatare_meniu():
    os.system('cls' if os.name == 'nt' else 'clear')