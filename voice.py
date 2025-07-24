import speech_recognition as sr

# Updated list of valid wake words
WAKE_WORDS = ["arise", "hey igris", "igris", "wake up igris", "wake up"]

def detect_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("IGRIS is listening for wake word...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        
    try:
        # Convert speech to lowercase text
        spoken_text = recognizer.recognize_google(audio).lower()
        print(f"You said: {spoken_text}")
        
        # Check if any wake word is in the spoken sentence
        for wake_word in WAKE_WORDS:
            if wake_word in spoken_text:
                return True
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")

    return False
