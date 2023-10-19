from TuyaSmartAPI import variaveis


tabela_intencoes_utterances = []
tabela_entidades = []
tabela_relacao_intencao_entidades = []
tabela_funcoes = []
tabela_relacao_intencao_funcoes = []

def addIntencao(intencao,utterances):
    global tabela_intencoes_utterances
    tabela_intencoes_utterances.append({intencao: utterances})
    #intencoes_utterances += [intencao,utterances]
    chave = list(tabela_intencoes_utterances[-1].keys())[0]
    return chave

def addEntidades(nome,entidades):
    global tabela_entidades
    tabela_entidades.append({nome:entidades})
    chave = list(tabela_entidades[-1].keys())[0]
    return chave

def addRelacaoIntencaoEntidades(chave_intencao,chave_entidades):
    global tabela_relacao_intencao_entidades
    utterances = ''
    entidades = ''
    for i in range(len(tabela_intencoes_utterances)):
        if list(tabela_intencoes_utterances[i].keys())[0] == chave_intencao:
            utterances = tabela_intencoes_utterances[i][chave_intencao]
            for j in range(len(tabela_entidades)):
                if list(tabela_entidades[j].keys())[0] == chave_entidades:
                    entidades = tabela_entidades[j][chave_entidades]
                    break
            break
    tabela_relacao_intencao_entidades.append([[utterances],[entidades]])
    return tabela_relacao_intencao_entidades

def addFuncoes(funcao,tipo,codigo):
    global tabela_funcoes
    #exec(codigo)
    print(codigo)
    tabela_funcoes.append((funcao,tipo,codigo))
    #print(tabela_funcoes)
    print(tabela_funcoes[0][2])
    return tabela_funcoes

def addRelacaoIntencaoFuncoes(chave_intencao,chave_funcao):
    global tabela_relacao_intencao_funcoes
    tabela_relacao_intencao_funcoes.append({chave_intencao:chave_funcao})
    chave = list(tabela_relacao_intencao_funcoes[-1].keys())[0]
    return chave
                    
    #tabela_relacao_intencao_entidades.append({intencao: entidades})
            
    
    

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