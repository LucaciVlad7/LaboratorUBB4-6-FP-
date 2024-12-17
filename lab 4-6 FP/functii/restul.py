import copy

class PachetCalatorie:
    def __init__(self, data_inceput, data_final, destinatie, pret):
        self.data_inceput = data_inceput
        self.data_final = data_final
        self.destinatie = destinatie
        self.pret = pret


class Agentie:
    def __init__(self):
        # Inițializăm lista de pachete de călătorie
        self.lista_pachete = []

    def adaugare_pachet(self, data_inceput, data_final, destinatie, pret):
        """
        Creeaza un pachet de calatorie nou
        :param data_inceput: cand incepe sejurul
        :param data_final: cand se termina sejurul
        :param destinatie: destinatia caltoriei
        :param pret: in lei
        """
        pachet = PachetCalatorie(data_inceput, data_final, destinatie, pret)
        self.lista_pachete.append(pachet)

    def modifica_pachet(self, data_inceput, data_final, destinatie, pret_nou):
        """
        Modifica pretul unui pachet de calatorie existent
        :param data_inceput: cand incepe sejurul care trebuie modificat
        :param data_final: cand se termina sejurul care trebuie modificat
        :param destinatie: destinatia sejurului care trebuie modificat
        :param pret_nou: Noul pret
        """
        for pachet in self.lista_pachete:
            if (pachet.data_inceput == data_inceput and
                pachet.data_final == data_final and
                pachet.destinatie == destinatie):
                pachet.pret = pret_nou

    def stergere_pachete_destinatie(self, destinatie):
        """
        Stergerea tuturor pachetelor de calatorie disponibile pentru o destinatie data
        :param destinatie: Destinatia care trebuie stearsa
        return: lista de pachete fara pachetele cu destinatia data
        """
        self.lista_pachete = [pachet for pachet in self.lista_pachete if pachet.destinatie != destinatie]

    def stergere_durata_scurta(self, nr_zile):
        """
        Sterge toate pachetele de calatorie care au o durata mai mica decat parametrul dat
        Se presupune ca un an are 365 de zile, iar o luna 30 de zile
        :param nr_zile: durata in zile
        :return: lista de pachete fara cele cu durata mai scurta decat nr_zile
        """
        pachete_de_sters = []
        for pachet in self.lista_pachete:
            zi_inceput, luna_inceput, an_inceput = map(int, pachet.data_inceput.split('.'))
            zi_final, luna_final, an_final = map(int, pachet.data_final.split('.'))

            # Calcularea duratei în zile
            durata = (an_final - an_inceput) * 365 + (luna_final - luna_inceput) * 30 + (zi_final - zi_inceput)

            if durata < nr_zile:
                pachete_de_sters.append(pachet)

        # Eliminăm pachetele care au durată mai scurtă
        self.lista_pachete = [pachet for pachet in self.lista_pachete if pachet not in pachete_de_sters]

    def stergere_pret_mai_mic(self, pret):
        """
        Stergerea tuturor pachetelor de calatorie care au pretul mai mare decat o suma data
        :param pret: Pretul pachetelor care trebuie sterse
        :return: lista cu pachete fara pachetele cu pretul mai mare parametrul pret
        """
        self.lista_pachete = [pachet for pachet in self.lista_pachete if pachet.pret >= pret]

    def pachete_in_interval(self, inceput_interval, sfarsit_interval):
        """
        Returneaza lista cu pachetele de calatorie dintr-un interval
        :param inceput_interval: inceputul intervalului
        :param sfarsit_interval: sfarsitul intervalului
        :return: lista cu pachete care se incadreaza intr-un interval
        """
        pachete_valide = []
        zi_inceput_int, luna_inceput_int, an_inceput_int = map(int, inceput_interval.split('.'))
        inceputI=zi_inceput_int+luna_inceput_int*30+an_inceput_int*365
        zi_sfarsit_int, luna_sfarsit_int, an_sfarsit_int = map(int, sfarsit_interval.split('.'))
        sfarsitI=zi_sfarsit_int+luna_sfarsit_int*30+an_sfarsit_int*365

        for pachet in self.lista_pachete:
            zi_inceput, luna_inceput, an_inceput = map(int, pachet.data_inceput.split('.'))
            inceputS=zi_inceput+luna_inceput*30+an_inceput*365
            zi_final, luna_final, an_final = map(int, pachet.data_final.split('.'))
            sfarsitS=zi_final+luna_final*30+an_final*365
            if (inceputI<=inceputS and sfarsitS<=sfarsitI):
                pachete_valide.append(pachet)

        return pachete_valide

    def pachete_destinatie_si_pret(self, destinatie, suma):
        """
        Returneaza pachetele cu o destinatie data si cu un pret mai mic decat parametrul suma
        :param destinatie: destinatia dorita
        :param suma: pretul trebuie sa fie mai mic ca acest parametru
        :return: lista cu pachete cu conditia data
        """
        pachete_valide = [pachet for pachet in self.lista_pachete if pachet.destinatie == destinatie and pachet.pret < suma]
        return pachete_valide

    def pachete_cu_data_final(self, data_sfarsit):
        """
        Returneaza pachetele care au o anumita data de sfarsit
        :param data_sfarsit: data de sfarsit dorita
        :return:lista cu pachetele care au data de final identica cu parametrul "data sfarsit"
        """
        pachete_valide = [pachet for pachet in self.lista_pachete if pachet.data_final == data_sfarsit]
        return pachete_valide

    def rapoarte_returnare_numar_oferte(self,destinatie):
        """
        returneaza numarul de pachete de calatorie care au o destinatie data
        :param destinatie: destinatia dorita
        """
        contor=0
        for pachet in self.lista_pachete:
            if pachet.destinatie==destinatie:
                contor+=1
        return contor

    def rapoarte_returnare_pachetelor_dintr_o_perioada(self,inceput_perioada,final_perioada):
        """
        Returneaza destinatia, perioada si pretul pachetelor de calatorie dintr-un interval dat
        :param inceput_perioada: inceputul periaodei dorite
        :param final_perioada: sfarsitul perioadei dorite
        """
        rezult=[]
        zi_inceput_int, luna_inceput_int, an_inceput_int = map(int, inceput_perioada.split('.'))
        inceputP = zi_inceput_int + luna_inceput_int * 30 + an_inceput_int * 365
        zi_sfarsit_int, luna_sfarsit_int, an_sfarsit_int = map(int, final_perioada.split('.'))
        sfarsitP = zi_sfarsit_int + luna_sfarsit_int * 30 + an_sfarsit_int * 365
        for pachet in self.lista_pachete:
            zi_inceput,luna_inceput,an_inceput=map(int,pachet.data_inceput.split('.'))
            pachet_inceput=zi_inceput+30*luna_inceput+365*an_inceput
            zi_final, luna_final, an_final = map(int, pachet.data_final.split('.'))
            pachet_final = zi_final + 30 * luna_final + 365 * an_final
            if inceputP<=pachet_inceput and pachet_final<=sfarsitP:
                rezult.append(pachet)
        rezult.sort(key=lambda pachet:pachet.pret)
        return rezult


    def rapoarte_returnare_medie_pret_a_unei_destinatii(self,destinatie):
        """
        Returneaza media de pret a unei destinatii dorite
        :param destinatie: destinatia dorita
        """
        contor=0
        suma=0
        for pachet in self.lista_pachete:
            if pachet.destinatie == destinatie:
                suma=suma+pachet.pret
                contor=contor+1
        medie=suma/contor
        return medie

    def filtrare_oferte_pretMaiMare_si_destinatieDiferita(self, pret, destinatie):
        """
        Filtreaza pachetele de calatorie prin adaugarea pachetelor cu un pret mai mic sau egal
        sau au o detinatie identica cu cea data ca parametru
        :param pret: Pretul care determina adaugarea in lista
        :param destinatie: Destinatia care determina adaugarea in lista un pret mai mic sau egal
        sau au o detinatie identica cu cea data ca parametru
        :return: lista filtrata, cu pachetele de calatorie care au un pret mai mic sau egal
        sau au o detinatie identica cu cea data ca parametru
        """
        listaFiltrata=[pachet for pachet in self.lista_pachete if pachet.pret<=pret or pachet.destinatie==destinatie]
        return listaFiltrata

    def filtrare_oferte_care_se_desfasoara_intro_anumita_luna(self,luna):
        """
        Filtreaza pachetele de calatorie prin agaugarea pachetelor care contin zile dintr-o
        luna data ca parametru
        :param luna: luna dorita trebuie sa apartina intervalului [1,12]
        :return: lista filtrata, cu pachetle care contin zile dintr-o luna, data ca parametru
        """
        rezultat=[]
        for pachet in self.lista_pachete:
            zi_inceput,luna_inceput,an_inceput=map(int, pachet.data_inceput.split('.'))
            zi_final, luna_final, an_final = map(int, pachet.data_final.split('.'))
            if luna_inceput<=luna and luna<=luna_final:
                rezultat.append(pachet)
        return rezultat

    def validare_pachet(self,data_inceput,data_final,destinatie,pret):
        """
            Functie care verifica daca:
                -data are 10 caractere si 3 puncte
                -data_inceput<data_final
                -pret pozitiv
            :param pachet: pachet de calatorie cu data_inceput, data_sfarsit, pret, destinatie
            :return: - daca pachet este valid
            :raises: ValueError cu mesajul "Data de inceput invalida!\n" daca data_inceput este invalid
                                           "Data de sfarsit invalid!\n" daca data_sfarsit este invalid
                                           "Pret invalid!\n" daca pretul este invalid
        """
        erori = ""
        if pret<= 0:
            erori += " Pret invalid!\n"
        contorPct=data_inceput.count('.')
        if len(data_inceput)!=10 and contorPct!=2:
            erori+="Data de inceput invalida!\n"
        contorPct = data_final.count('.')
        if len(data_final) != 10 and contorPct != 2:
            erori += "Data de sfarsit invalida!\n"
        zi1,luna1,an1=map(int, data_inceput.split('.'))
        suma1=zi1+30*luna1+365*an1
        zi2, luna2, an2 = map(int, data_final.split('.'))
        suma2=zi2+30*luna2+365*an2
        if suma1>suma2:
            erori+="Data de inceput este mai mare decat cea de sfarsit\n"
        if not (1<=zi1 and zi1<=31):
            erori+="ziua de inceput este invalida\n"
        if not(1<=luna1 and luna1<=12):
            erori+="Luna de inceput este invalida\n"
        if not(an1>=2024):
            erori+="Anul de inceput este invalid\n"

        if not (1<=zi2 and zi2<=31):
            erori+="ziua de sfarsit este invalida\n"
        if not(1<=luna2 and luna2<=12):
            erori+="Luna de sfarsit este invalida\n"
        if not(an2>=2024):
            erori+="Anul de sfarsit este invalid\n"
        return erori

def test():
    agentie = Agentie()

    # Adăugare pachete
    agentie.adaugare_pachet("01.06.2024", "10.06.2024", "Paris", 3000)
    agentie.adaugare_pachet("15.07.2024", "25.07.2024", "Roma", 2500)
    agentie.adaugare_pachet("01.08.2024", "05.08.2024", "Paris", 1500)

    # Test pentru adaugare_pachet
    assert len(agentie.lista_pachete) == 3

    # Test pentru modifica_pachet
    agentie.modifica_pachet("01.08.2024", "05.08.2024", "Paris", 1800)
    assert agentie.lista_pachete[2].pret == 1800

    # Test pentru stergere_pachete_destinatie
    agentie.stergere_pachete_destinatie("Paris")
    assert len(agentie.lista_pachete) == 1  # Doar pachetul pentru "Roma" rămâne

    # Test pentru stergere_durata_scurta
    agentie.adaugare_pachet("01.09.2024", "9.09.2024", "Berlin", 4000)
    agentie.stergere_durata_scurta(9)
    assert len(agentie.lista_pachete) == 1  # Pachetul "Roma" ramane

    # Test pentru stergere_pret_mai_mic
    agentie.stergere_pret_mai_mic(3000)
    assert len(agentie.lista_pachete) == 0 # sterge Roma

    # Test pentru pachete_in_interval
    agentie.adaugare_pachet("15.12.2024", "25.12.2024", "Tokyo", 5000)
    interval_pachete = agentie.pachete_in_interval("01.12.2024", "31.12.2024")
    assert len(interval_pachete) == 1
    assert interval_pachete[0].destinatie == "Tokyo"

    # Test pentru pachete_destinatie_si_pret
    pachete_paris = agentie.pachete_destinatie_si_pret("Tokyo", 10000)
    assert len(pachete_paris) == 1 # tokyo

    # Test pentru pachete_cu_data_final
    pachete_final = agentie.pachete_cu_data_final("25.12.2024")
    assert len(pachete_final) == 1
    assert pachete_final[0].destinatie == "Tokyo"

    # Test pentru rapoarte_returnare_numar_oferte
    nr_oferte_roma = agentie.rapoarte_returnare_numar_oferte("Tokyo")
    assert nr_oferte_roma == 1

    # Test pentru rapoarte_returnare_pachetelor_dintr_o_perioada
    agentie.adaugare_pachet("02.07.2024","03.07.2024","Londra",1000)
    pachete_in_perioada = agentie.rapoarte_returnare_pachetelor_dintr_o_perioada("01.07.2024", "31.12.2024")
    assert len(pachete_in_perioada) == 2  # Include "Londra" și "Tokyo"
    assert all(pachete_in_perioada[i].pret <= pachete_in_perioada[i + 1].pret for i in range(len(pachete_in_perioada) - 1)) # crescator in fct de pret

    # Test pentru rapoarte_returnare_medie_pret_a_unei_destinatii
    agentie.adaugare_pachet("01.10.2024", "15.10.2024", "Londra", 3000)
    medie_londra = agentie.rapoarte_returnare_medie_pret_a_unei_destinatii("Londra")
    assert medie_londra == 2000  # Media pentru "Londra"

    # Test pentru filtrare_oferte_pretMaiMare_si_destinatieDiferita
    filtrate_pret = agentie.filtrare_oferte_pretMaiMare_si_destinatieDiferita(4000, "Londra")
    assert len(filtrate_pret) == 2  # Include pachetele cu preț <= 4000 și destinația "Londra"

    # Test pentru filtrare_oferte_care_se_desfasoara_intro_anumita_luna
    pachete_in_luna = agentie.filtrare_oferte_care_se_desfasoara_intro_anumita_luna(12)
    assert len(pachete_in_luna) == 1  # Pachetul "Tokyo"

    print("Toate testele merg")

if __name__ == "__main__":
    test()
