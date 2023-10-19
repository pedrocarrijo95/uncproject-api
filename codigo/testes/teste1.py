#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

from threading import Thread
import threading
import time
from queue import Queue

import speech_recognition as sr


r = sr.Recognizer()
audio_queue = Queue()


def recognize_worker():
    # this runs in a background thread
    while True:
        audio = audio_queue.get()  # retrieve the next audio processing job from the main thread
        if audio is None: break  # stop processing if the main thread is done

        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            reconhecido = r.recognize_google(audio, language='pt-BR')
            print("Google Speech Recognition thinks you said " + reconhecido)
            if 'tarefa' in reconhecido:
                print('comando reconhecido')
                threading.Thread(target=teste()).start()

                    
                    
            if 'cancelar' in reconhecido:
                print('cancelado')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        audio_queue.task_done()  # mark the audio processing job as completed in the queue

def teste():
    for i in range(15):
        print(i,flush=True)
        time.sleep(1)
# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with sr.Microphone() as source:
    try:
        while True:  # repeatedly listen for phrases and put the resulting audio on the audio processing job queue
            r.adjust_for_ambient_noise(source,3)
            audio_queue.put(r.listen(source))
    except KeyboardInterrupt:  # allow Ctrl + C to shut down the program
        pass

audio_queue.join()  # block until all current audio processing jobs are done
audio_queue.put(None)  # tell the recognize_thread to stop
recognize_thread.join()  # wait for the recognize_thread to actually stop