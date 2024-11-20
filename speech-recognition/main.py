import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source:
    print("Say something:")
    # Listen for the first phrase and extract it into audio data
    audio_data = recognizer.listen(source)
    print("Recognizing...")

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
