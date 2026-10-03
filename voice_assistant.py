import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)

recognizer = sr.Recognizer()

while True:

    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        if "hello" in text.lower():
            print("Hello! How can I help you?")
            engine.say("Hello! How can I help you?")
            engine.runAndWait()

        if "youtube" in text.lower():
            print("Opening YouTube...")
            engine.say("Opening YouTube")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com")

        if "search" in text.lower():
            search_query = text.lower().replace("search", "").strip()

            print("Searching for:", search_query)

            engine.say("Searching for " + search_query)
            engine.runAndWait()

            webbrowser.open(
                "https://www.google.com/search?q=" + search_query
            )

        if "time" in text.lower():
            current_time = datetime.now().strftime("%I:%M %p")
            print("The time is", current_time)
            engine.say("The time is " + current_time)
            engine.runAndWait()

        if "date" in text.lower():
            current_date = datetime.now().strftime("%d %B %Y")
            print("Today's date is", current_date)
            engine.say("Today's date is " + current_date)
            engine.runAndWait()

        if "note" in text.lower():
            note = text.lower().replace("note", "").strip()

            with open("voice_notes.txt", "a") as file:
                file.write(note + "\n")

            print("Note saved:", note)

            engine.say("Note saved")
            engine.runAndWait()

        if "exit" in text.lower():
            engine.say("Goodbye")
            engine.runAndWait()
            break

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

    except sr.RequestError:
        print("Could not connect to the speech recognition service.")