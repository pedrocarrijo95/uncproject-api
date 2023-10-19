#pip3 install tuya-connector-python
#pip3 install tuya-iot-py-sdk

from tuya_connector import TuyaOpenAPI
import time
from TuyaSmartAPI import variaveis


def conectarTuyaAPI(API_ENDPOINT,ACCESS_ID,ACCESS_KEY):
    openapi = TuyaOpenAPI(API_ENDPOINT,ACCESS_ID,ACCESS_KEY)
    openapi.connect()
    return openapi


openapi = conectarTuyaAPI(variaveis.API_ENDPOINT,variaveis.ACCESS_ID,variaveis.ACCESS_KEY)


#Funções para controle dos dipositivos

def ligar_desligar(flag,id_dispositivo):
    #response = openapi.get("/v1.0/iot-03/devices/"+variaveis.SMARTBULB_ID+"/specification")
    #print(response)
    commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
    responseCommand = openapi.post("/v1.0/iot-03/devices/"+id_dispositivo+"/commands",commands)
    print(responseCommand)
    
def mudar_cor(cor_hsv,id_dispositivo,branca):
    print(cor_hsv)
    commands = {'commands': [{'code': 'colour_data_v2', 'value': {'h':cor_hsv[0],'s':cor_hsv[1],'v':cor_hsv[2]} }]}
    if branca:
       commands = {'commands': [{'code': 'work_mode', 'value': 'white' }]} 
    responseCommand = openapi.post("/v1.0/iot-03/devices/"+id_dispositivo+"/commands",commands)
    print(responseCommand)
    


