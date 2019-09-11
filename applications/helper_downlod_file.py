import requests


# requests.get('https://api.github.com/user', auth=requests.auth.HTTPBasicAuth('user', 'pass'))
# TO DO
# Acessar Email, Abrir email X assunto, Copiar link do botão "ver boleto atualizado

url = 'https://hsacondominios.superlogica.net/clients/areadocondomino/publico/cobranca/c/68073-0c1f36a86282d135d6bac098b02c50d43909fd27-flSegundaVia-palbuquerque@lopes.com.br;condominios@quintoandar.com.br'
myfile = requests.get(url, allow_redirects=True)
open('C:/Lab/python/applications/Thainazinha.pdf', 'wb').write(myfile.content)

