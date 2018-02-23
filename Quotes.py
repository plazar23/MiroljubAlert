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
    Citat = Postovi[i].find('div', class_='quote')
    PomocnaLista = Postovi[i].split(str(Citat))
    # AAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaAAAAAAAA
    # Probaj sa find_all i splituj sa svakim itemom iz liste. Ali nije toliki problem sa splitovanjem koliki je sa ponovnim sastavljanejm
    # Mislim da je kljuc svega "".join()!!!
    # Uzmi string Postovi[i] splituj sa Citat[j] {j je u opsegu od nula do n [n = len(Citat)]}
    # Na Citat[j] dodati <italic> -----  Citat[j] = '<italic>' + Citat[j] + '</italic>'
    # Iteme iz pomocne liste spojiti sa "Citat[j]"
    forumHTML.write(str(Postovi[i].prettify()))
    citatiHTML.write(str(Citat) + '\n' + '\n' + '\n')
