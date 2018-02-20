from bs4 import BeautifulSoup  # Ukljucujemo biblioteku za Parsovanje HTML-a
import requests  # Ukljucujemo biblioteku za rad sa URL-om
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sredinahtmla = str()

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

me = "miroljubalert@gmail.com"
you = "plazar23@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "NOVI POSTOVI NA FORUMU"
msg['From'] = me
msg['To'] = you

pocetakhtmla = '<html><head></head><body><p>'
krajhtmla = '</p></body></html>'

brojPosta = 0

while (brojPosta % 20) == 0:
    pomocni = open('pomocni.txt', 'r', encoding="utf-8")
    brojLinije = 0
    for line in pomocni:
        newline = line.rstrip()
        if brojLinije == 0:
            ukupnoPostova = int(newline)  # ucitavamo iz pomocnog fajla
        elif brojLinije == 1:
            stariBrojPosta = int(newline)
        brojLinije = brojLinije + 1

    adresaForuma = 'http://www.creation6days.com/diskusije/forum/viewthread.php?thread_id=4&rowstart=' + str(ukupnoPostova)  # ukupnoPostova

    source = requests.get(adresaForuma).text
    soup = BeautifulSoup(source, 'lxml')  # Ukljucujemo lxml parser, mogli smo i html5lib da odaberemo

    # forumHTML = open('forumHTML.txt', 'w', encoding="utf-8")  # Da bih mogao lakše i preglednije da imam uvid u HTML foruma
    Postovi = soup.find_all('td', class_='tbl1 forum_thread_user_post')
    brojPosta = len(Postovi)  # Odnosi se na broj postova na datoj strani. Max 20!

    for i in range(stariBrojPosta, brojPosta):
        sredinahtmla = sredinahtmla + '<p><br><br>' + str(Postovi[i].prettify()) + '</p>'
    # forumHTML.write(str(sredinahtmla))

    html = pocetakhtmla + sredinahtmla + krajhtmla
    sredinahtmla = ''
    part = MIMEText(html, 'html')
    msg.attach(part)

    if stariBrojPosta != brojPosta:
        mail.login(me, 'idespodmac')
        mail.sendmail(me, you, msg.as_string())

    if brojPosta == 20:
        brojPosta = 0
        ukupnoPostova = ukupnoPostova + 20

    pomocni = open('pomocni.txt', 'w', encoding="utf-8")
    pomocni.write(str(ukupnoPostova) + '\n' + str(brojPosta))

mail.quit()
