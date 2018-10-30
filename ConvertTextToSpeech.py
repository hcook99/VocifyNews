from gtts import gTTS
from langdetect import detect
import TextHandler

def getMP3FromText(text):
    lang = detectDialect(text)
    audioSpeech = gTTS(text, lang)
    audioSpeech.save("static/temp.mp3")

def detectDialect(text):
    try:
        lang = detect(text)
        return lang
    except:
        return None