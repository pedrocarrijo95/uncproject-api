import requests
import json
#import unc_variaveis as unc_vars
from UncSoftwareAPI import unc_variaveis


def getlistaItem(item_ativo = "S",sql_limit = 100,sql_offset = 0):
    url = unc_variaveis.GET_LISTA_ITEMS_ENDPOINT

    payload = json.dumps({
    "ITEM_ATIVO": item_ativo, #S
    "SQL_LIMIT": sql_limit, #100
    "SQL_OFFSET": sql_offset #0
    })
    headers = unc_variaveis.HEADERS

    response = requests.request("PUT", url, headers=headers, data=payload)

    #Tratar para pegar somente os campos item_codigo e item_descricao
    lista_items = response.json()["result"][0]["Conteudo"]["DADOS"]
    items = []
    for i in range(len(lista_items)):
        items.append([lista_items[i]["item_codigo"],lista_items[i]["item_descricao"]])


    #print(response)
    return items


''' Qual é o estoque do item 0000000016 - cola retapur '''
def getEstoque(item_id):
    url = unc_variaveis.GET_ESTOQUE_ENDPOINT

    payload = json.dumps({
    "EMPRESA_INICIAL": "001",
    "EMPRESA_FINAL": "999",
    "ESTOQUESALDO_DTVALIDADEINICIAL": "1900-01-01",
    "ESTOQUESALDO_DTVALIDADEFINAL": "2999-12-31",
    "ESTSALDODATA_DATA": "2023-07-10",
    "DEPOSITO_CODIGO": "",
    "LOCALIZACAO_CODIGO": "",
    "ITEM_CODIGOREFERENCIA": item_id,
    "ESTOQUESALDO_NROLOTE": "",
    "GRUPOESTOQUE_CODIGO": "",
    "FAMCOMERCIAL_CODIGO": "",
    "GRUPOESTOQUE_TIPO": "",
    "ESTOQUESALDO_NEGATIVO": "0",
    "ESTOQUESALDO_COMSALDO": "0",
    "ESTOQUESALDO_MENORQTDESEGURANCA": "0",
    "ITEM_CONTROLAESTOQUE": "-1",
    "ESTOQUESALDO_SALDOZERO": "0",
    "FILTRO_ITEMCOMSALDO": "-1",
    "FILTRO_ITEMCOMSALDODIFZERO": "0"
    })
    headers = unc_variaveis.HEADERS

    response = requests.request("PUT", url, headers=headers, data=payload)

    quantidade = response.json()["result"][0]["Conteudo"]["DADOS"][0]["estsaldodata_qtdedisponivel"]
    print(response)
    for j in range(5):
        for k in range(2):
            print(j,k)
    return quantidade


'''Método acima criado pelo código direto


Para criarmos utilizando LowCode: nossa ferramenta precisaria se comunicar diretamente com o banco para querys


Na hora de configurar a entidade, se caso tiver que buscar no banco de dados, vamos precisar flagar uma caixinha para afirmar que é DB, e colocar o nome da tabela juntamente com campo_chave e campo_valor (exemplo: item_descricao,item_codigo)
Na hora de configurar a resposta colocariamos o endpoint,headers,body etc.. e codificariamos em ? a tratativa dessa resposta (teriamos em mãos o valor da entidade detectada basta utilizar a variavel)

'''
