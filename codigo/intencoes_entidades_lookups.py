from TuyaSmartAPI import variaveis
from PostgreeSql import connect as banco


tabela_intencoes_enunciados = []
tabela_entidades = []
tabela_relacao_intencao_entidades = []
tabela_funcoes = []
tabela_relacao_intencao_funcoes = []
tabela_apis = []


def attIntencoes():
    global tabela_intencoes_enunciados
    conn = banco.conectarBanco()
    cursor = conn.cursor()


    selectIntencoes = "SELECT int_id,int_descricao,int_enunciado FROM intencao"
    cursor.execute(selectIntencoes)
    tabela_intencoes_enunciados = cursor.fetchall()
    cursor.close()
    conn.close()
    
def attEntidades():
    global tabela_entidades
    conn = banco.conectarBanco()
    cursor = conn.cursor()

    selectEntidades = "SELECT ent_id,ent_descricao,ent_entidade,func_id FROM entidade"
    cursor.execute(selectEntidades)
    tabela_entidades = cursor.fetchall()
    cursor.close()
    conn.close()
    
def attRelacoes():
    global tabela_relacao_intencao_entidades
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    
    selectRelacoesIntencoesEntidades = "SELECT r.intent_id,i.int_enunciado,e.ent_entidade,e.func_id,f.func_fonte FROM intencao_entidade r LEFT JOIN intencao i ON r.int_id = i.int_id LEFT JOIN entidade e ON r.ent_id = e.ent_id LEFT JOIN funcao f ON r.func_id = f.func_id" #inner join para trazer descricoes
    cursor.execute(selectRelacoesIntencoesEntidades)
    tabela_relacao_intencao_entidades = cursor.fetchall()

    cursor.close()
    conn.close()
    
def attFuncoes():
    global tabela_funcoes
    conn = banco.conectarBanco()
    cursor = conn.cursor()

    selectFuncoes = "SELECT func_id,func_nome,func_fonte,func_tipo FROM funcao"
    cursor.execute(selectFuncoes)
    tabela_funcoes = cursor.fetchall()
    cursor.close()
    conn.close()
    
def attAPI():
    global tabela_apis
    conn = banco.conectarBanco()
    cursor = conn.cursor()

    selectAPIs = "SELECT api_id,api_json FROM api"
    cursor.execute(selectAPIs)
    tabela_apis = cursor.fetchall()
    cursor.close()
    conn.close()
    



def atualizarTabelas():
    #atualiza todas abaixo
    attIntencoes()
    attEntidades()
    attRelacoes()
    attFuncoes()
    attAPI()

atualizarTabelas()


def addIntencao(descricao,enunciados):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    insert_query = f"""INSERT INTO intencao (int_descricao,int_enunciado) VALUES ('{descricao}','{enunciados}')"""
    cursor.execute(insert_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return descricao

def addEntidades(descricao,entidades,func_id = None):
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    if func_id != None:
        insert_query = f"""INSERT INTO entidade (ent_descricao,ent_entidade,func_id) VALUES ('{descricao}','{entidades}',{func_id})"""
        cursor.execute(insert_query)
    else:    
        insert_query = f"""INSERT INTO entidade (ent_descricao,ent_entidade) VALUES ('{descricao}','{entidades}')"""
        cursor.execute(insert_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return descricao

def addRelacaoIntencaoEntidades(int_id,ent_id,func_id = None):
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    if func_id != None:
        insert_query = f"""INSERT INTO intencao_entidade (int_id,ent_id,func_id) VALUES ('{int_id}','{ent_id}',{func_id})"""
        cursor.execute(insert_query)
    else:
        insert_query = f"""INSERT INTO intencao_entidade (int_id,ent_id) VALUES ('{int_id}','{ent_id}')"""
        cursor.execute(insert_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return tabela_relacao_intencao_entidades

def addFuncoes(func_nome,func_fonte,tipo):
    global tabela_funcoes

    #tabela_funcoes.append((funcao,tipo,codigo))
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    print(func_nome,func_fonte,tipo)
    insert_query = f"""INSERT INTO funcao (func_nome,func_fonte,func_tipo) VALUES ('{func_nome}','{func_fonte}','{tipo}')"""
    cursor.execute(insert_query) #usar aspas duplas no codigo
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return func_nome

def addAPI(api_json):
    global tabela_funcoes

    #tabela_funcoes.append((funcao,tipo,codigo))
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    insert_query = f"""INSERT INTO api (api_json) VALUES ('{api_json}')"""
    cursor.execute(insert_query) #usar aspas duplas no codigo
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return api_json

def updateIntencao(int_id,descricao,enunciados):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    update_query = f"""
        UPDATE intencao
        SET int_descricao = '{descricao}', int_enunciado = '{enunciados}'
        WHERE int_id = {int_id}
    """
    cursor.execute(update_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return descricao

def updateEntidades(ent_id,descricao,entidades,func_id = None):
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    if func_id != None:
        update_query = f"""
            UPDATE entidade
            SET ent_descricao = '{descricao}', ent_entidade = '{entidades}', func_id = {func_id}
            WHERE ent_id = {ent_id}
        """
        cursor.execute(update_query)
    else:    
        update_query = f"""
            UPDATE entidade
            SET ent_descricao = '{descricao}', ent_entidade = '{entidades}'
            WHERE ent_id = {ent_id}
        """
        cursor.execute(update_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return descricao

def updateRelacaoIntencaoEntidade(intent_id,int_id,ent_id,func_id = None):
    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    if func_id != None:
        update_query = f"""
            UPDATE intencao_entidade
            SET int_id = '{int_id}', ent_id = '{ent_id}', func_id = {func_id}
            WHERE id = {intent_id}
        """
        cursor.execute(update_query)
    else:    
        update_query = f"""
            UPDATE intencao_entidade
            SET int_id = '{int_id}', ent_id = '{ent_id}'
            WHERE intent_id = {intent_id}
        """
        cursor.execute(update_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()
    atualizarTabelas()
    return intent_id

def updateFuncoes(func_id,func_nome,func_fonte,tipo):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    update_query = f"""
        UPDATE funcao
        SET func_nome = '{func_nome}', func_fonte = '{func_fonte}', func_tipo = '{tipo}'
        WHERE func_id = {func_id}
    """
    cursor.execute(update_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return func_id


def updateAPI(api_id,api_json):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    update_query = f"""
        UPDATE api
        SET api_json = '{api_json}'
        WHERE api_id = {api_id}
    """
    cursor.execute(update_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return api_id

def deleteIntencao(int_id):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    delete_query = f"""
        DELETE FROM intencao WHERE int_id = {int_id}
    """
    cursor.execute(delete_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return int_id

def deleteEntidade(ent_id):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    delete_query = f"""
        DELETE FROM entidade WHERE ent_id = {ent_id}
    """
    cursor.execute(delete_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return ent_id

def deleteFuncao(func_id):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    delete_query = f"""
        DELETE FROM funcao WHERE func_id = {func_id}
    """
    print(delete_query)
    cursor.execute(delete_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return func_id

def deleteRelacaoIntencaoEntidade(intent_id):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    delete_query = f"""
        DELETE FROM intencao_entidade WHERE ent_id = {intent_id}
    """
    cursor.execute(delete_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return intent_id

def deleteAPI(api_id):
    # Criar um cursor para executar comandos SQL

    conn = banco.conectarBanco()
    cursor = conn.cursor()
    # Executar uma consulta
    # Consulta SQL de atualização
    delete_query = f"""
        DELETE FROM api WHERE api_id = {api_id}
    """
    cursor.execute(delete_query)
    banco.conn.commit()
    # Fechar o cursor
    cursor.close()
    conn.close()

    #intencoes_enunciados += [intencao,enunciados]
    atualizarTabelas()
    return api_id

            
      

#Frases de reconhecimento de INTENÇÕES
frases_acordar = [
    'olá',
    'bom dia',
    'boa tarde',
    'oi',
    'salve',
    'acordar',
    'está por aí',
    'tá por aí',
    'cadê você',
    'preciso de você',
    'acorda',
    'e aí',
]
frases_toque = [
    'toque',
    'tocar',
    'ouvir'
]
frases_horario = [
    'horas',
    'horário',
    'relógio',
    'data'
]
frases_tempo = [
    'tempo',
    'previsão',
    'meteorológico',
    'temperatura',
    'chovendo',
    'chover',
    'nublado',
    'quente',
    'frio'
]
frases_alterar_cidade = [
    'alterar cidade',
    'alterar a cidade',
    'alterar essa cidade',
    'mudar cidade',
    'mudar essa cidade',
    'mudar a cidade',
    'editar cidade',
    'editar essa cidade',
    'editar a cidade',
    'modificar cidade',
    'modificar essa cidade',
    'modificar a cidade',
    'outra cidade',
    'alterar',
    'editar'
]
frases_gratidao = [
    'obrigado',
    'obrigada'
    'agradeço',
    'grato',
    'valeu',
    'tamo junto'
]
frases_descansar = [
    'descansar',
    'cochilar',
    'pausar',
    'pausa',
    'parar',
    'dormir',
    'dorme',
    'tchau'
]
frases_duvidas = [
    'dúvidas',
    'questões',
    'questionamentos',
    'perguntas',
    'gpt',
    'chat gpt',
    'dúvida'
]
frases_garota_bonita = [
    'mais bonita',
    'mais linda',
    'maravilhosa',
    'linda',
    'mais estilosa',
    'estilosa'
]
frases_garoto_bonito = [
    'mais bonito',
    'mais lindo',
    'maravilhoso',
    'lindo',
    'mais estiloso',
    'estiloso'
]
frases_despedida_gpt = [
    'voltar',
    'sair',
    'tchau',
    'obrigado'
]
frases_cotacao_moeda = [
    'valor',
    'cotação',
]
frases_noticias = [
    'notícias',
    'artigos'
]
frases_email = [
    'e-mail',
    'email',
    'mensagem',
    'recado'
]
frases_capacidades = [
    'capacidades',
    'habilidades',
    'poderes',
    'funcionalidades',
    'sabe fazer'
]
#---
frases_tuya = [
    'ligar', #0
    'acender', #1
    'ativar', #2
    'habilitar', #3
    'desativar', #4
    'apagar', #5
    'desabilitar', #6
    'mudar cor', #7
    'alterar cor', #8
    'mudar a cor', #9
    'cor', #10
]
ligar_range = [0,4]
apagar_range = [4,7]
mudar_range = [7,11]
#---




#ENTIDADES
entidades_cidades = [
    'americana',
    'pereira barreto',
    'rio de janeiro',
    'são paulo',
    'rio claro',
    'minas gerais',
    'minas',
    'salvador',
    'fernando de noronha',
    'nova york',
    'paris',
    'teresina'
]
entidades_cotacao = [
    'dólar',
    'euro',
    'libra',
    'btc'
]
entidades_noticias = [
    'hoje',
    'semana',
    'mês'
]

#---
entidades_tuya = [
    #Dispositivo LuzSala
    'luz sala',
    'sala',
    'modo cinema',
    #Dispostivio luzFundo
    'luz fundo',
    'fundo',
    'modo jogo',
    #Cores
    'vermelho',
    'rosa',
    'roxo',
    'azul',
    'amarelo',
    'ciano',
    'verde',
    'laranja',
    "branca",
    "normal",
]

luzsala_range = [0,3]
luzfundo_range = [3,6]
#---

vazia = []

#Lookups necessários
lookup_cotacao = [
    [entidades_cotacao[0],'USD'],
    [entidades_cotacao[1],'EUR'],
    [entidades_cotacao[2],'GBP'],
    [entidades_cotacao[3],'BTC']
]

lookup_noticias = [
    [entidades_noticias[0], 1],
    [entidades_noticias[1], 7],
    [entidades_noticias[2], 30]
]

#TUYA SMART INTENÇÕES    
lookup_tuya_intencoes= []
#Monta lookup INTENÇÕES TUYA passando start,stop,step em um loop pelas INTENÇÕES, populando o valor das partes igualmente
#Para cada "for" varrida do array, adicionar o id do dispositivo

#1.Ligar
for i in range(ligar_range[0], ligar_range[1], 1): #start,stop,step
    sublist = frases_tuya[i:i+1]
    sublist.extend(['ligar'])
    lookup_tuya_intencoes.append(sublist)

#2.Apagar
for i in range(apagar_range[0], apagar_range[1], 1): #start,stop,step
    sublist = frases_tuya[i:i+1]
    sublist.extend(['apagar'])
    lookup_tuya_intencoes.append(sublist)
    
#2.Mudar
for i in range(mudar_range[0], mudar_range[1], 1): #start,stop,step
    sublist = frases_tuya[i:i+1]
    sublist.extend(['mudar'])
    lookup_tuya_intencoes.append(sublist)
#print(lookup_tuya_intencoes)

#TUYA SMART ENTIDADES (DISPOSITIVOS)
lookup_tuya_entidades= []

#1.Luz Sala
for i in range(luzsala_range[0], luzsala_range[1], 1): #start,stop,step
    sublist = entidades_tuya[i:i+1]
    sublist.extend([variaveis.LUZSALA_ID])
    lookup_tuya_entidades.append(sublist)

#2.Luz Fundo
for i in range(luzfundo_range[0], luzfundo_range[1], 1): #start,stop,step
    sublist = entidades_tuya[i:i+1]
    sublist.extend([variaveis.LUZFUNDO_ID])
    lookup_tuya_entidades.append(sublist)   
#print(lookup_tuya_entidades)
    
lookup_tuya_cores = [
    [entidades_tuya[6],0,1000,500], #vermelho
    [entidades_tuya[7],350,1000,500], #rosa
    [entidades_tuya[8],300,1000,500], #roxo
    [entidades_tuya[9],240,1000,500], #azul
    [entidades_tuya[10],60,1000,500], #amarelo
    [entidades_tuya[11],180,1000,500], #ciano
    [entidades_tuya[12],120,1000,500], #verde
    [entidades_tuya[13],39,1000,500], #laranja
    [entidades_tuya[14],0,0,0], #branca
    [entidades_tuya[15],0,0,0], #normal
]
    

#Matriz de relação INTENÇÃO -> ENTIDADES
relacoes_int_ent = [
    [frases_acordar, vazia],
    [frases_toque,vazia],
    [frases_horario, entidades_cidades],
    [frases_tempo, entidades_cidades],
    [frases_alterar_cidade,entidades_cidades],
    [frases_gratidao,vazia],
    [frases_descansar,vazia],
    [frases_duvidas,vazia],
    [frases_garota_bonita,vazia],
    [frases_garoto_bonito,vazia],
    [frases_cotacao_moeda,entidades_cotacao],
    [frases_noticias,entidades_noticias],
    [frases_email,vazia],
    [frases_capacidades,vazia],
    [frases_tuya,entidades_tuya]
]