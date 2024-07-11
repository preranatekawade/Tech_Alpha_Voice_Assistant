import speech_recognition as sr
import pyttsx3
import DateTime

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        user_command = listen_for_command()
        if "hello" in user_command:
            speak("Hello! How can I assist you today?")
        elif "time" in user_command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "exit" in user_command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
