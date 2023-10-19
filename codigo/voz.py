import speech_recognition as sr
import pyttsx3
import time
import variaveis
from pygame import mixer

def configurarListener():
    listener = sr.Recognizer()
    listener.energy_threshold = 35000
    listener.pause_threshold = 2
    return listener

def configurarEnginePyttsx():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')
    engine.setProperty("voice", "brazil")
    return engine

def configurarBeep():
    mixer.init()
    plays = mixer.Sound('./sons/beep.mp3')
    plays.set_volume(0.2)
    return plays    
    

listener = configurarListener()
engine = configurarEnginePyttsx()
plays = configurarBeep()

def talk(text):
    engine.say(text)
    engine.runAndWait()


#with sr.Microphone() as source:
#    listener.adjust_for_ambient_noise(source,duration = variaveis.TEMPO_CALIBRAGEM+2)
tempo_inicial = time.time()
def take_command():
    global tempo_inicial
    try:
        command = ''
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration = variaveis.TEMPO_CALIBRAGEM)
            print('escutando ...')
            if variaveis.BEEP:
                plays.play()
            time.sleep(0.5)
            voice = listener.listen(source,phrase_time_limit = variaveis.LIMITE_TEMPO_FRASE)
            command = listener.recognize_google(voice,language='pt-BR')
            command = command.lower()
            if variaveis.NOME_ASSISTENTE in command:
                command = command.replace(variaveis.NOME_ASSISTENTE, '')
                variaveis.PALAVRA_ASSISTENTE = True
                variaveis.BEEP = True
                print(command)
                return command
    except Exception as err:     
        print(err)
    return command

def resposta_pergunta_assistent():
    command = ''
    try:
        with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source,3)
                print('escutando resposta...')
                if variaveis.BEEP:
                    plays.play()
                time.sleep(0.5)
                voice = listener.listen(source,phrase_time_limit=variaveis.LIMITE_TEMPO_FRASE)
                command = listener.recognize_google(voice,language='pt-BR')
                command = command.lower()
    except Exception:
        pass
    return command
