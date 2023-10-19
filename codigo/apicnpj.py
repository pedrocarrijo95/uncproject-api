import requests

url = "https://receitaws.com.br/v1/cnpj/23154573000175"

# Fazer a solicitação GET à API
response = requests.get(url)

# Verificar se a resposta da API é bem-sucedida (código de status 200)
if response.status_code == 200:
    # Converter a resposta JSON em um objeto Python
    data = response.json()

    # Acessar um atributo específico do JSON
    nome_empresa = data["nome"]

    # Imprimir o valor do atributo
    resposta = f"Nome da empresa: {nome_empresa}"
else:
    print("Falha na solicitação. Código de status:", response.status_code)
