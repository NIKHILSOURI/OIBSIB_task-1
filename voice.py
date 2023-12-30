import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
from datetime import datetime

def speak(text):
    # Convert text to speech and play it
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

def recognize_speech():
    # Recognize speech using Google Speech Recognition
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            speak(f"Searching the web for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("What would you like me to search for?")
    else:
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you today?")

    while True:
        user_input = recognize_speech()

        if user_input:
            handle_command(user_input)
