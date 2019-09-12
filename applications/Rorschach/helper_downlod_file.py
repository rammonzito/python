import requests
import LinksFromHeaven
import Xeretador
import re

msg = Xeretador.Xeretador.read_email_from_gmail()
# print(msg)
# msg = re.sub(r"\s+", "", msg, flags=re.UNICODE)
links = LinksFromHeaven.LinksFromHeaven.extract(msg)
print (msg)

# for l in links:
#     print(l)
# print(file)
# myfile = requests.get(url, allow_redirects=True)
# open('C:/Lab/python/applications/Thainazinha.pdf', 'wb').write(myfile.content)
