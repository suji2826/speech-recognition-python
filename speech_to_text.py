import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print("\nYou Said:")
    print(text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not connect to Google Speech Recognition service.")