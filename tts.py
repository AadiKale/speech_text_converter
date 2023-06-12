import pyttsx3
import sounddevice as sd

from speech_recognition import Microphone

speak = pyttsx3.init()
#speak.setProperty("rate", 100)
text = "Hello bhargavi"
#speak.say(text)

voices = speak.getProperty("voices")
# print(voices)
speak.setProperty("rate", 150)
speak.setProperty("voice", voices[1].id)

# text2 = "voice change successful"
speak.say(text)
speak.setProperty("voice", voices[0].id)
speak.say(text)
speak.runAndWait()


