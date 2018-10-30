from aylienapiclient import textapi
import ConvertTextToSpeech

class TextHandler:
    client = textapi.Client('**********', '***************************')
    def __init__(self, urlEntryS):
        self.invalidURL = True
        try:
            self.dataExtracted = self.client.Extract(urlEntryS)
        except textapi.HttpError:
            self.invalidURL = False
    def isValid(self):
        return self.invalidURL
    def getTitle(self):
        self.title = self.dataExtracted["title"]
        return self.title
    def getArticle(self):
        self.article = self.dataExtracted["article"]
        return self.article
    def getAudio(self):
        fullText = self.title + '\n' + self.article
        if ConvertTextToSpeech.detectDialect(fullText) is None:
            self.invalidURL=False
        else:
            ConvertTextToSpeech.getMP3FromText(fullText)


