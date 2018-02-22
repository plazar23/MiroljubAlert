from bs4 import BeautifulSoup  # Ukljucujemo biblioteku za Parsovanje HTML-a
import requests  # Ukljucujemo biblioteku za rad sa URL-om

ukupnoPostova = 38700

adresaForuma = 'http://www.creation6days.com/diskusije/forum/viewthread.php?thread_id=4&rowstart=' + str(ukupnoPostova)  # ukupnoPostova

source = requests.get(adresaForuma).text
soup = BeautifulSoup(source, 'lxml')  # Ukljucujemo lxml parser, mogli smo i html5lib da odaberemo

# Users = soup.find_all('td', class_='tbl2 forum_thread_user_info')

forumHTML = open('forumHTML.html', 'w', encoding="utf-8")  # Da bih mogao lakše i preglednije da imam uvid u HTML foruma

# for User in Users:
#     forumHTML.write(str(User.prettify()))
forumHTML.write(str(soup.prettify()))
