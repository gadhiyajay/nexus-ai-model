import speech_recognition as sr
import pyttsx3
import sounddevice


def say(str):
    speaker = pyttsx3.init()
    speaker.say(str)
    speaker.runAndWait()


say("Hello, This is Nexus, How are you Today??")


def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Nexus Listening..!")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            print(text)
            return text.lower()

    except Exception:
        print("Please Speak Again!")


listen()
