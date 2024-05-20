import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    #aqui é como um dicionário (vazio)
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            #se o nome do restaurante não estiver dentro de dados do restaurante
            dados_restaurante[nome_do_restaurante] = []
            #se n tiver vai criar uma lista
        
        dados_restaurante[nome_do_restaurante].append({
            #e aqui vai adicionar na lista
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
        #aqui já conseguimos acessar os dados dos restaurantes


else: 
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)

#fiz uma nota pra explicar isso no notion chamada criando arquivos