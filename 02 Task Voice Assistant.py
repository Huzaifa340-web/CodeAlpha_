import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a request error.")
            return None

def wish_user():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def execute_task(query):
    if 'play' in query:
        song = query.replace('play', '')
        speak(f"Playing {song}")
        kit.playonyt(song)
    elif 'wikipedia' in query:
        topic = query.replace('wikipedia', '')
        speak(f"Searching Wikipedia for {topic}")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    elif 'open' in query:
        website = query.replace('open', '').strip()
        speak(f"Opening {website}")
        webbrowser.open(website)
    elif 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {str_time}")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye, have a great day!")
        exit()

def main():
    wish_user()
    while True:
        query = listen()
        if query:
            execute_task(query)

if __name__ == "__main__":
    main()
