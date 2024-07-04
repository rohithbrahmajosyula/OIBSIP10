import wikipedia
import pyttsx3
from datetime import datetime
import speech_recognition as sr


def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        voice("hello, i am voice assistant! how can i help you")
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None


def voice(response):
    engine = pyttsx3.init()

    engine.setProperty("rate", 180)
    engine.say(response)
    engine.runAndWait()


def web_search(req):
    return wikipedia.summary(req, sentences=2)


current_time = datetime.now().strftime("%H:%M:%S")


request = listen_for_command()
if request:
    if request == "hello":
        voice("hello, I am voice assistant")
    elif "time" in request:
        voice(current_time)
    else:
        voice(web_search(request))



