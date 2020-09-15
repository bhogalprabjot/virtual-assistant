import speech_recognition as sr 
import os
import pyttsx3


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said {}'.format(command))
    except sr.UnknownValueError:
        print("....")
        command = myCommand()
    return command


def botResponse(audio):
    print(audio)
    engine = pyttsx3.init()
    for line in audio.splitlines():
        engine.say(line)
        engine.runAndWait()

