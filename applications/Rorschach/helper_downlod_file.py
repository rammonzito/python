import requests
import LinksFromHeaven
import Xeretador
import re

msg = Xeretador.Xeretador.read_email_from_gmail()
links = LinksFromHeaven.LinksFromHeaven.extract(msg)

for url in links:
    NOME_PDF = "PDF_Legal_"
    i = 0
    print("Don't worry, The pdf is being prepared.. ;)")
    myfile = requests.get(url, allow_redirects=True)
    open('C:/Lab/python/applications/' + NOME_PDF + str(i) + '.pdf', 'wb').write(myfile.content)
    i = i + 1
