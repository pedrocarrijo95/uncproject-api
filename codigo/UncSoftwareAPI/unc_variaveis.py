#Base para API
ENDPOINT_BASE = "https://api.uncsoftware.com.br/API_UNC/datasnap/rest"
USUARIO = "MASTER"
SENHA = "MASTER"

#Endpoints para comandos
GET_ESTOQUE_ENDPOINT = ENDPOINT_BASE+"/TWSEstoque_Saldo/GetListaNaData"
GET_LISTA_ITEMS_ENDPOINT = ENDPOINT_BASE+"/TWSItem/GetPorCampos"


#Variaveis para header
PUB_SISTEMA = "EMPRESARIAL"
PUB_USUARIO_EMAIL = "teste.api@unicodesoftware.com.br"
AUTHORIZATION_BASE64 = "Basic TUFTVEVSOk1BU1RFUg=="





#Header padrão
HEADERS = {
    'PubSistema': PUB_SISTEMA,
    'PubUsuarioEmail': PUB_USUARIO_EMAIL,
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_BASE64
}
