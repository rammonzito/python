import requests
import json

api = "https://localhost:44357/api/product"

response = requests.get(api, verify=False)
# print(response.status_code)
# print(response.content)

produtos = json.loads(response.content)

# headers = {
#     'content-type': 'application/json',
# }
# params = (
#     ('priority', 'normal'),
# )


for p in produtos:
    print(p['marca'])

dados = data = { "Marca" : "Adidas", "Cor" : "Amarelo", "Ano" : 2020, "Colecao" : "Back to the future" }
# print(dados)

response = requests.post(api, json = dados, verify=False)
print(response.status_code)

