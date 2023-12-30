# OIBSIB_task-1
project about Voice assistant in python 

This Python script is a basic implementation of a voice-controlled assistant using speech recognition and text-to-speech synthesis. Here's a breakdown of the code:

1. **Import Libraries:**
   - `speech_recognition`: Library for performing speech recognition.
   - `gtts (gTTS)`: Google Text-to-Speech API wrapper for text-to-speech synthesis.
   - `os`: Provides a way of using operating system-dependent functionality.
   - `webbrowser`: Allows displaying web-based documents to users.
   - `datetime`: Library for working with dates and times.

2. **Functions:**
   - `speak(text)`: Takes a text input, converts it to an MP3 file using Google Text-to-Speech, and plays the generated audio file.
   - `recognize_speech()`: Uses the microphone to capture audio, applies noise adjustment, and recognizes speech using Google Speech Recognition. Returns the recognized speech as a lowercase string or `None` if speech is not recognized.
   - `handle_command(command)`: Takes a recognized command and performs actions based on certain keywords. It can greet the user, provide the current time or date, search Google for a specified query, or prompt the user to repeat if the command is not recognized.

3. **Main Execution:**
   - The script starts by greeting the user and asking how it can assist.
   - It enters a continuous loop where it listens to the user's speech input using `recognize_speech()`.
   - If speech is recognized (`user_input` is not `None`), it processes the input using `handle_command()`.
   - The `handle_command()` function checks for specific keywords like "hello," "time," "date," or "search" and responds accordingly.

4. **Specific Commands:**
   - "hello": The assistant greets the user.
   - "time": Provides the current time.
   - "date": Provides the current date.
   - "search": Performs a Google search based on the following query.

5. **Note:**
   - The assistant relies on Google Speech Recognition, so an internet connection is required.
   - The webbrowser module is used to open a Google search for the specified query.
   - The assistant continuously listens for commands until manually stopped.

This script serves as a simple example and can be extended with additional functionalities or enhanced for more sophisticated interactions with the user.
