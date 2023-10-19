import autopep8

codigo = 'def consulta_cnpj(cnpj):\n     url = f"https://api.receitaws.com.br/v1/cnpj/{cnpj}"\n     resposta = None\n          try:\n         response = requests.get(url)\n         data = response.json()\n                  if response.status_code == 200:\n             resposta = data\n         else:\n             resposta = {"error": data["message"]}\n     except requests.exceptions.RequestException as e:\n         resposta = {"error": str(e)}\n          return resposta\n  # Insira um CNPJ válido para consulta cnpj_consulta = "12345678901234"  # Substitua pelo CNPJ desejado  resposta = consulta_cnpj(cnpj_consulta)'
codigo_identado = autopep8.fix_code(codigo)

print('a')
print(codigo_identado)

exec(codigo_identado)


for i in range(5):
    for j in range(2):
        for l in range(6):
            print(i,j,l);
            
for token in range(2):
    print("fora do for inicial");