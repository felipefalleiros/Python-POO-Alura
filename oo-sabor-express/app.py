import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# get para solicitar a  informação
response = requests.get(url)
# Output <Response [200]> significa que a requisição (get) foi bem sucedida
print(response)

# 200 é o status code da variável response
if response.status_code == 200:
    # Acessando os dados JSON
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        # Acessando o nome dos restaurantes através dos valores da chave 'Company'
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            # Cria uma chave contendo o nome do restaurante e seu valor é uma lista vazia
            dados_restaurante[nome_do_restaurante] = []
        # Adiciona as informações do restaurante acessando os valores das chaves e armazenando na lista que é o valor da chave nome_do_restaurante
        dados_restaurante[nome_do_restaurante].append({
            "item":item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

# Cria um arquivo para cada restaurante
# Acessando as chaves (nome_do_restaurante) e o valor (dados) do dicionario dados_restaurantes
for nome_do_restaurante, dados in dados_restaurante.items():
    # Atribuindo o nome do restaurante para o nome do arquivo
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # Abre o arquivo em modo de escrita
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        # Serializa / Salva os dados para o arquivo_restaurante
        json.dump(dados, arquivo_restaurante, indent=4)
