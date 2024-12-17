from pydoc import describe

from functii.restul import Agentie
import copy
from meniu import *

lista_undo = []#stack
ag = Agentie()

def handle_command(comanda):
    """
    Manageriaza ce functie sa apeleze in functie de input
    :param comanda: numarul comenzi dorite
    """
    match comanda:
        case 0:
            print("Programul se va inchide")
            exit(0)
        case 1:#merge
            print("Ati ales comanda Adaugare Pachet de Calatorie")
            print("__________________________________________________________")
            try:
                data_inceput=input("Introduceti data de inceput cu formatul DD.MM.YYYY: ")
                data_final=input("Introduceti data de final cu formatul DD.MM.YYYY: ")
                destinatie=input("Introduceti destinatia: ")
                pret=int(input("Introduceti pretul: "))
                lista_undo.append(ag.lista_pachete[:])
                erori=ag.validare_pachet(data_inceput,data_final,destinatie,pret)
                if len(erori)>0:
                    raise ValueError("Pachetul nu este valid")
                else:
                    ag.adaugare_pachet(data_inceput,data_final,destinatie,pret)
            except ValueError:
                print("Eroare! Ati introdus una sau mai multe valori invalide asa ca pachetul nu va fi adaugat")
        case 2:#merge
            print("Ati ales comanda Modifica Pachet de Calatorie")
            print("__________________________________________________________")
            try:
                data_inceput = input("Introduceti data de inceput a pachetului care trebuie modificat cu formatul DD.MM.YYYY: ")
                data_final = input("Introduceti data de final a pachetului care trebuie modificat cu formatul DD.MM.YYYY: ")
                destinatie = input("Introduceti destinatia a pachetului care trebuie modificat: ")
                pretNou = int(input("Introduceti noul pretul: "))
                lista_undo.append(ag.lista_pachete[:])
                ag.modifica_pachet(data_inceput,data_final,destinatie,pretNou)
            except ValueError:
                print("Eroare! Ati introdus una sau mai multe valori invalide")
        case 3:#merge
            print("Ati ales comanda Stergere Pachete in functie de Destinatie")
            print("__________________________________________________________")
            try:
                destinatie = input("Introduceti destinatia pachetului care va fi stearsa: ")
                lista_undo.append(ag.lista_pachete[:])
                ag.stergere_pachete_destinatie(destinatie)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 4:#merge
            print("Ati ales comanda Stergere Pachete in functie de Durata")
            print("__________________________________________________________")
            try:
                nr_zile=int(input("Introduceti durata, in zile, astfel in cat pachetele cu o durata mai scurta sa fie sterse"))
                lista_undo.append(ag.lista_pachete[:])
                ag.stergere_durata_scurta(nr_zile)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 5:#merge
            print("Ati ales comanda Stergere Pachete de Calatorie cu Pret mai mic "
                  "decat cel transmis prin parametru")
            print("__________________________________________________________")
            try:
                pret=int(input("Introduceti pretul astfel incat pachetele cu pret mai mic vor fi sterse: "))
                lista_undo.append(ag.lista_pachete[:])
                ag.stergere_pret_mai_mic(pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 6:#merge
            print("Ati ales comanda care returneaza pachetele dintr-un interval dat")
            print("__________________________________________________________")
            try:
                inceput_interval=input("Inceputul intervalului dorit cu formatul DD.MM.YYYY: ")
                sfarsit_interval=input("Sfarsitului intervalului dorit cu formatul DD.MM.YYYY: ")
                ag.rezult=ag.pachete_in_interval(inceput_interval, sfarsit_interval)
                contor=0
                for pachet in ag.rezult:
                        contor=contor+1
                        print("-------------------")
                        print(f"Pachetul {contor}")
                        print(pachet.data_inceput)
                        print(pachet.data_final)
                        print(pachet.destinatie)
                        print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 7:#merge
            print("Ati ales comanda care afiseaza pachetele cu o destinatie data si cu"
                  " un pret mai mic decat parametrul dat")
            print("__________________________________________________________")
            try:
                destinatie=input("Introduceti destinatia: ")
                pret=int(input("Introduceti pretul: "))
                ag.rezult=ag.pachete_destinatie_si_pret(destinatie,pret)
                contor = 0
                for pachet in ag.rezult:
                        contor=contor+1
                        print("-------------------")
                        print(f"Pachetul {contor}")
                        print(pachet.data_inceput)
                        print(pachet.data_final)
                        print(pachet.destinatie)
                        print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 8:#merge
            print("Ati ales comdanda care returneaza pachetele cu o anumita data de sfarsit")
            print("__________________________________________________________")
            try:
                sfarsitPachet=input("Introduceti Sfarsitul perioadei dupa urmatorul format DD.MM.YYYY: ")
                ag.rezult=ag.pachete_cu_data_final(sfarsitPachet)
                contor = 0
                for pachet in ag.rezult:
                        contor=contor+1
                        print("-------------------")
                        print(f"Pachetul {contor}")
                        print(pachet.data_inceput)
                        print(pachet.data_final)
                        print(pachet.destinatie)
                        print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 9:#rapoarte 1,merge
            print("Ati ales comanda care afiseaza pe ecran numarul de oferte pentru o destinatie data")
            print("__________________________________________________________")
            try:
                destinatie=input("Introduceti destinatia dorita: ")
                contor=ag.rapoarte_tiparire_numar_oferte(destinatie)
                print(f"Numarul de pachete cu destinatia {destinatie} este: {contor}")
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 10:#rapoarte 2,merge
            print("Ati ales comada care afiseaza toate ofertele dintr-o perioada data in ordine crescatoare a pretului")
            print("__________________________________________________________")
            try:
                inceput_perioada=input("Introduceti inceputul perioadei dorite cu formatul DD.MM.YYYY: ")
                sfarsit_perioda=input("Introduceti sfarsitul perioadei dorite cu formatul DD.MM.YYYY: ")
                rezult=ag.rapoarte_tiparire_pachetelor_dintr_o_perioada(inceput_perioada,sfarsit_perioda)
                for pachet in rezult:
                    print("--------------")
                    print(pachet.destinatie)
                    print(pachet.data_inceput)
                    print(pachet.data_final)
                    print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 11:#rapoarte 3, merge
            print("Ati ales comanda care afiseaza media de pret a ofertelor pentru o destinatie dorita")
            print("__________________________________________________________")
            try:
                destinatie=input("Introduceti destinatia dorita: ")
                rez=ag.rapoarte_tiparire_medie_pret_a_unei_destinatii(destinatie)
                print(rez)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 12:#merge, prima filtrare
            print("Ati ales comanda care filtreaza pachetele de calatorie "
                  "prin tiparirea pachetelor cu un pret mai mic sau egal"
                "sau au o detinatie identica cu cea data ca parametru")
            print("__________________________________________________________")
            try:
                pret=int(input("Introduceti pretul dorit: "))
                destinatie=input("introduceti destinatia dorita: ")
                ag.rezult=ag.filtrare_oferte_pretMaiMare_si_destinatieDiferita(pret,destinatie)
                contor = 0
                for pachet in ag.rezult:
                        contor=contor+1
                        print("-------------------")
                        print(f"Pachetul {contor}")
                        print(pachet.data_inceput)
                        print(pachet.data_final)
                        print(pachet.destinatie)
                        print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 13:#filtrare 2,merge
            print("Ati ales comanda care filtreaza pachetele de calatorie "
                "prin tiparirea pachetelor care contin zile dintr-o luna"
                  "data")
            print("__________________________________________________________")
            try:
                luna=int(input("Introduceti luna dorit: "))
                ag.rezult=ag.filtrare_oferte_care_se_desfasoara_intro_anumita_luna(luna)
                for pachet in ag.rezult:
                    contor = 0
                    for pachet in ag.rezult:
                        contor = contor + 1
                        print("-------------------")
                        print(f"Pachetul {contor}")
                        print(pachet.data_inceput)
                        print(pachet.data_final)
                        print(pachet.destinatie)
                        print(pachet.pret)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case 14:
            if lista_undo:
                print("Ati ales comanda undo, astfel efectul ultimei functii a fost anulat")
                ag.lista_pachete = lista_undo.pop()  # Restabilire stare anterioara
            else:
                print("Nu se poate efectua undo")
        case 100:#merge
            """
            Printeaza sirul curent retinui in ag.lista_pachete
            """
            contor=0
            if ag.lista_pachete:
                for pachet in ag.lista_pachete:
                    contor = contor + 1
                    print("-------------------")
                    print(f"Pachetul {contor}")
                    print(pachet.data_inceput)
                    print(pachet.data_final)
                    print(pachet.destinatie)
                    print(pachet.pret)
            else:
                print("Lista cu pachete este goala")
        case _:
            print("Comanda nu exista!")

def handle_command_cuvinte(curent,parametri):
    match curent:
        case "gata":
            print("Programul se va inchide")
            exit(0)
        case "adauga":
            print("Ati ales comanda Adaugare Pachet de Calatorie")
            print("__________________________________________________________")
            try:
                lista_date_intrare=parametri.split(",")
                data_inceput=lista_date_intrare[0]
                data_final=lista_date_intrare[1]
                destinatie=lista_date_intrare[2]
                pret=int(lista_date_intrare[3])
                lista_undo.append(ag.lista_pachete[:])
                erori = ag.validare_pachet(data_inceput, data_final, destinatie, pret)
                if len(erori) > 0:
                    raise ValueError("Pachetul nu este valid")
                else:
                    ag.adaugare_pachet(data_inceput, data_final, destinatie, pret)
            except ValueError:
                print("Eroare! Ati introdus una sau mai multe valori invalide asa ca pachetul nu va fi adaugat")
        case "modifica":
            print("Ati ales comanda Modifica Pachet de Calatorie")
            print("__________________________________________________________")
            try:
                #data_inceput = input("Introduceti data de inceput a pachetului care trebuie modificat cu formatul DD.MM.YYYY: ")
                #data_final = input("Introduceti data de final a pachetului care trebuie modificat cu formatul DD.MM.YYYY: ")
                #destinatie = input("Introduceti destinatia a pachetului care trebuie modificat: ")
                #pretNou = int(input("Introduceti noul pretul: "))
                lista_date_intrare=parametri.split(",")
                data_inceput = lista_date_intrare[0]
                data_final = lista_date_intrare[1]
                destinatie = lista_date_intrare[2]
                pretNou = int(lista_date_intrare[3])
                lista_undo.append(ag.lista_pachete[:])
                ag.modifica_pachet(data_inceput, data_final, destinatie, pretNou)
            except ValueError:
                print("Eroare! Ati introdus una sau mai multe valori invalide")
        case "stergere":
            print("Ati ales comanda Stergere Pachete in functie de Destinatie")
            print("__________________________________________________________")
            try:
                #destinatie = input("Introduceti destinatia pachetului care va fi stearsa: ")
                lista_cu_destinatie=parametri.split(",")
                destinatie=lista_cu_destinatie[0]
                lista_undo.append(ag.lista_pachete[:])
                ag.stergere_pachete_destinatie(destinatie)
            except ValueError:
                print("Eroare! Ati introdus o valoare invalida")
        case "undo":
            if lista_undo:
                print("Ati ales comanda undo, astfel efectul ultimei functii a fost anulat")
                ag.lista_pachete = lista_undo.pop()  # Restabilire stare anterioara
            else:
                print("Nu se poate efectua undo")
        case "afisare":  # merge
            """
            Printeaza sirul curent retinui in ag.lista_pachete
            """
            contor = 0
            if ag.lista_pachete:
                for pachet in ag.lista_pachete:
                    contor = contor + 1
                    print("-------------------")
                    print(f"Pachetul {contor}")
                    print(pachet.data_inceput)
                    print(pachet.data_final)
                    print(pachet.destinatie)
                    print(pachet.pret)
            else:
                print("Lista cu pachete este goala")
        case _:
            print("Comanda nu exista!")


def main():
    print("Select Mode: \n"
          "1. Normal Mode\n"
          "2. Batch Mode\n"
          "Press '0' for exit\n")
    mode=int(input("Introduceti modul dorit: "))
    match mode:
        case 1:
            while(True):
                #meniu()
                #curatare_meniu()
                try:
                    comanda=int(input("Introduceti Comanda>> "))
                    handle_command(comanda)
                except ValueError:
                    print("Eroare! Comanda trebuie sa fie un numar")
        case 2:
            while (True):
            # meniu()
            # curatare_meniu()
                try:
                    lista_comenzi0 = input("Introduceti Comenzile folosind cuvinte sau 'gata' pentru a iesi\n"
                                "Dupa comanda vor urma parametri functiei aferente, separate printr-0 virgula, iar apoi ';' pentru a separa functia"
                                ">> ")
                    lista_comenzi1=lista_comenzi0.split(";")
                    for curent in lista_comenzi1:
                        lst=curent.split(" ")
                        if len(lst)>1:
                            handle_command_cuvinte(lst[0],lst[1])
                        else:
                            lst.append(" ")
                            handle_command_cuvinte(lst[0], lst[1])
                except ValueError:
                    print("Eroare! Comanda trebuie sa fie un ")
        case 0:
            print("Programul se va inchide")
            exit(0)
        case _:
            print("Acest mod nu exista")

if __name__ == "__main__":
    main()