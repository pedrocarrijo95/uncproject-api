from flask import Flask, request
#import main
import intencoes_entidades_lookups
import funcoes
import variaveis

app = Flask(__name__)

@app.route('/main',methods=['POST'])
def main():
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()
    # Verifica se 'descricao' e 'enunciado' estão presentes nos dados
    if 'comando' in data:
        comando = data['comando']
        #resposta = 'local'
        resposta = funcoes.run_assistente(comando)
        if resposta != "" and resposta != " " and resposta != None:
            return resposta
        return 'resposta não encontrada'
    else:
        return variaveis.MENSAGEM_ERRO_API
    #comando =  request.args.get('comando')
    #resposta = run_assistente()
    #if resposta != "" and resposta != " ":
        #return resposta
    #return 'comando enviado'
    
#INSERTS 
@app.route('/addIntencao',methods=['POST'])
def addIntencao():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'descricao' e 'enunciado' estão presentes nos dados
    if 'int_descricao' in data and 'int_enunciado' in data:
        descricao = data['int_descricao']
        enunciados = data['int_enunciado']
        return intencoes_entidades_lookups.addIntencao(descricao,enunciados)
    else:
        return variaveis.MENSAGEM_ERRO_API
    #descricao =  request.args.get('descricao')
    #enunciados =  request.args.get('enunciado')

@app.route('/addEntidade',methods=['POST'])
def addEntidade():
    #ent_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()
    print("DATA="+str(data))
    # Verifica se 'ent_descricao' e 'ent_entidade' estão presentes nos dados
    if 'ent_descricao' in data and 'ent_entidade' in data:
        descricao = data['ent_descricao']
        entidade = data['ent_entidade']
        print(data['func_id'])
        if(data['func_id'] != '' and data['func_id'] != None and data['func_id'] != 0):
            func_id = data['func_id']
        else:
            func_id = None
        return intencoes_entidades_lookups.addEntidades(descricao,entidade,func_id)
    else:
        return variaveis.MENSAGEM_ERRO_API


@app.route('/addRelacaoIntencaoEntidades',methods=['POST'])
def addRelacaoIntecaoEntidades():
    #intent_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'int_id' e 'ent_id' estão presentes nos dados
    if 'int_id' in data and 'ent_id' in data:
        int_id = data['int_id']
        ent_id = data['ent_id']
        if(data['func_id'] != ''):
            func_id = data['func_id']
        else:
            func_id = None
        return intencoes_entidades_lookups.addRelacaoIntencaoEntidades(int_id,ent_id,func_id)
    else:
        return variaveis.MENSAGEM_ERRO_API


@app.route('/addFuncao',methods=['POST'])
def addFuncao():
    #func_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'func_nome' e 'func_fonte' estão presentes nos dados
    if 'func_nome' in data and 'func_fonte' in data:
        func_nome = data['func_nome']
        func_fonte = data['func_fonte']
        if(data['func_tipo'] != ''):
            tipo = data['func_tipo']
        else:
            tipo = None
        return intencoes_entidades_lookups.addFuncoes(func_nome,func_fonte,tipo)
    else:
        return variaveis.MENSAGEM_ERRO_API

@app.route('/addAPI',methods=['POST'])
def addFuncao():
    #func_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'func_nome' e 'func_fonte' estão presentes nos dados
    if 'api_json' in data:
        api_json = data['api_json']
        return intencoes_entidades_lookups.addAPI(api_json)
    else:
        return variaveis.MENSAGEM_ERRO_API


#GETS 
@app.route('/getIntencoes')
def getIntencoes():
    intencoes_entidades_lookups.attIntencoes()
    print(intencoes_entidades_lookups.tabela_intencoes_enunciados)
    
    lista_de_dicionarios = funcoes.getJsonIntencoes()
    
    print(lista_de_dicionarios)
    return lista_de_dicionarios

@app.route('/getEntidades')
def getEntidades():
    intencoes_entidades_lookups.attEntidades()
    
    lista_de_dicionarios = funcoes.getJsonEntidades()
    
    print(lista_de_dicionarios)
    return lista_de_dicionarios

@app.route('/getRelacaoIntencaoEntidade')
def getRelacaoIntencaoEntidade():
    intencoes_entidades_lookups.attRelacoes()
    
    lista_de_dicionarios = funcoes.getJsonRelacoes()
    
    print(lista_de_dicionarios)
    return lista_de_dicionarios   

@app.route('/getFuncoes')
def getFuncoes():
    intencoes_entidades_lookups.attFuncoes()
    
    lista_de_dicionarios = funcoes.getJsonFuncoes()
    
    print(lista_de_dicionarios)
    return lista_de_dicionarios   

@app.route('/getAPIs')
def getAPIs():
    intencoes_entidades_lookups.attAPI()
    
    lista_de_dicionarios = funcoes.getJsonAPIs()
    
    print(lista_de_dicionarios)
    return lista_de_dicionarios  

@app.route('/')
def retornarTabelas():
    #a = unc.getEstoque('0000000001')
    #print(str(a))
    intencoes_entidades_lookups.atualizarTabelas()
    return 'Intenções: '+str(intencoes_entidades_lookups.tabela_intencoes_enunciados) + '<br><br>Entidades: '+ str(intencoes_entidades_lookups.tabela_entidades) + '<br><br>Relações (Intenções -> Entidades): ' + str(intencoes_entidades_lookups.tabela_relacao_intencao_entidades) + '<br><br>Funções: '+ str(intencoes_entidades_lookups.tabela_funcoes) + '<br><br>Relações (Intenções -> Funções): '+ str(intencoes_entidades_lookups.tabela_relacao_intencao_funcoes)


#UPDATES
@app.route('/updateIntencao',methods=['PUT'])
def updateIntencao():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'int_id', 'descricao' e 'enunciado' estão presentes nos dados
    if 'int_id' in data and 'int_descricao' in data and 'int_enunciado' in data:
        int_id = data['int_id']
        descricao = data['int_descricao']
        enunciados = data['int_enunciado']
        return intencoes_entidades_lookups.updateIntencao(int_id,descricao,enunciados)
    else:
        return variaveis.MENSAGEM_ERRO_API

@app.route('/updateEntidade',methods=['PUT'])
def updateEntidade():
    #ent_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'ent_id', 'descricao' e 'entidade' estão presentes nos dados
    if 'ent_id' in data and 'ent_descricao' in data and 'ent_entidade' in data:
        ent_id = data['ent_id']
        descricao = data['ent_descricao']
        entidade = data['ent_entidade']
        if(data['func_id'] != ''):
            func_id = data['func_id']
        else:
            func_id = None
        return intencoes_entidades_lookups.updateEntidades(ent_id,descricao,entidade,func_id)
    else:
        return variaveis.MENSAGEM_ERRO_API

@app.route('/updateRelacaoIntencaoEntidade',methods=['PUT'])
def updateRelacaoIntencaoEntidade():
    #intent_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'intent_id', 'int_id' e 'ent_id' estão presentes nos dados
    if 'intent_id' in data and 'int_id' in data and 'ent_id' in data:
        intent_id = data['intent_id']
        int_id = data['int_id']
        ent_id = data['ent_id']
        if(data['func_id'] != ''):
            func_id = data['func_id']
        else:
            func_id = None
        return intencoes_entidades_lookups.updateRelacaoIntencaoEntidade(intent_id,int_id,ent_id,func_id)
    else:
        return variaveis.MENSAGEM_ERRO_API

@app.route('/updateFuncao',methods=['PUT'])
def updateFuncao():
    #func_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'func_nome' e 'func_fonte' estão presentes nos dados
    if 'func_id' in data and 'func_nome' in data and 'func_fonte' in data:
        func_id = data['func_id']
        func_nome = data['func_nome']
        func_fonte = data['func_fonte']
        if(data['func_tipo'] != ''):
            tipo = data['func_tipo']
        else:
            tipo = None
        return intencoes_entidades_lookups.updateFuncoes(func_id,func_nome,func_fonte,tipo)
    else:
        return variaveis.MENSAGEM_ERRO_API
    
@app.route('/updateAPI',methods=['PUT'])
def updateAPI():
    #func_id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    # Verifica se 'api_id' e 'api_json' estão presentes nos dados
    if 'api_id' in data and 'api_json':
        api_id = data['api_id']
        api_json = data['api_json']
        return intencoes_entidades_lookups.updateAPI(api_id,api_json)
    else:
        return variaveis.MENSAGEM_ERRO_API

#DELETES
@app.route('/deleteIntencao',methods=['DELETE'])
def deleteIntencao():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    if 'int_id' in data:
        int_id = data['int_id']
        return intencoes_entidades_lookups.deleteIntencao(int_id)
    else:
        return variaveis.MENSAGEM_ERRO_API
    
@app.route('/deleteEntidade',methods=['DELETE'])
def deleteEntidade():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    if 'ent_id' in data:
        ent_id = data['ent_id']
        return intencoes_entidades_lookups.deleteEntidade(ent_id)
    else:
        return variaveis.MENSAGEM_ERRO_API
    
@app.route('/deleteFuncao',methods=['DELETE'])
def deleteFuncao():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    if 'func_id' in data:
        func_id = data['func_id']
        return intencoes_entidades_lookups.deleteFuncao(func_id)
    else:
        return variaveis.MENSAGEM_ERRO_API
    
@app.route('/deleteRelacaoIntencaoEntidade',methods=['DELETE'])
def deleteRelacaoIntencaoEntidade():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    if 'intent_id' in data:
        intent_id = data['intent_id']
        return intencoes_entidades_lookups.deleteRelacaoIntencaoEntidade(intent_id)
    else:
        return variaveis.MENSAGEM_ERRO_API

@app.route('/deleteAPI',methods=['DELETE'])
def deleteAPI():
    #id auto_increment
    # Obtém os dados do corpo da solicitação em formato JSON
    data = request.get_json()

    if 'api_id' in data:
        api_id = data['api_id']
        return intencoes_entidades_lookups.deleteAPI(api_id)
    else:
        return variaveis.MENSAGEM_ERRO_API
