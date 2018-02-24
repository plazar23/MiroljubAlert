from bs4 import BeautifulSoup  # Ukljucujemo biblioteku za Parsovanje HTML-a
import requests  # Ukljucujemo biblioteku za rad sa URL-om

ukupnoPostova = 38700

adresaForuma = 'http://www.creation6days.com/diskusije/forum/viewthread.php?thread_id=4&rowstart=' + str(ukupnoPostova)  # ukupnoPostova

forumHTML = open('forumHTML.html', 'w', encoding="utf-8")  # Da bih mogao lakše i preglednije da imam uvid u HTML foruma
citatiHTML = open('citatiHTML.html', 'w', encoding="utf-8")

source = requests.get(adresaForuma).text
soup = BeautifulSoup(source, 'lxml')  # Ukljucujemo lxml parser, mogli smo i html5lib da odaberemo

Postovi = soup.find_all('td', class_='tbl1 forum_thread_user_post')


for i in range(0, 20):
    # AAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaAAAAAAAA
    # Probaj sa find_all i splituj sa svakim itemom iz liste. Ali nije toliki problem sa splitovanjem koliki je sa ponovnim sastavljanejm
    # Mislim da je kljuc svega "".join()!!!
    # Uzmi string Postovi[i] splituj sa Citat[j] {j je u opsegu od nula do n [n = len(Citat)]}
    # Na Citat[j] dodati <italic> -----  Citat[j] = '<italic>' + Citat[j] + '</italic>'
    # Iteme iz pomocne liste spojiti sa "Citat[j]"
    Citat = Postovi[i].find_all('div', class_='quote')
    n = len(Citat)
    for j in range(0, n):
        if Citat[j] is not None:                                        # Ova linija <3
            PomocnaLista = str(Postovi[i]).split(str(Citat[j]))
            Citat[j] = "<i><b>" + str(Citat[j]) + "</b></i>"
            # PomocniString = "PomocniCitat".join(str(PomocnaLista))  Nazalost nije Dobijali smo fajl sa gomilom izraza izmedju navodnika!
            # Proverimo da li pomocna Lista ima 1 ili 2 clana Na Miroljubovom forumu citat je ili na pocetku ili u sredini!
            # Ako je odgovor 1 napisemo da je Postovi[i] = str(Citat[j]) + str(PomocnaLista[0])
            # Ako je odgovor 2 napisemo da je Postovi[i] = str(PomocnaLista[0]) + str(Citat[j]) + str(PomocnaLista[1])
            if len(PomocnaLista) == 1:
                Postovi[i] = str(Citat[j]) + str(PomocnaLista[0])
            elif len(PomocnaLista) == 2:
                Postovi[i] = str(PomocnaLista[0]) + str(Citat[j]) + str(PomocnaLista[1])
    forumHTML.write(str(Postovi[i]))
    citatiHTML.write(str("<br>".join(Citat)))
