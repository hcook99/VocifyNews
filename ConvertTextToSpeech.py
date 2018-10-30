from gtts import gTTS
from langdetect import detect
import TextHandler

def getMP3FromText(text):
    try:
        audioSpeech = gTTS(text, lang=detectDialect(text))
        audioSpeech.save("static/temp.mp3")
    except:
        TextHandler.TextHandler.invalidURL = False

def detectDialect(text):
    try:
        lang = detect(text)
        return lang
    except:
        TextHandler.TextHandler.invalidURL = False