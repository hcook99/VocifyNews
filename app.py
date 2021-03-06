from flask import Flask, render_template, request, redirect, url_for
from TextHandler import TextHandler

app = Flask(__name__)

@app.route('/')
def main_app_render():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def response():
    text = request.form['urlEntry']
    handler = TextHandler(text)
    if handler.isValid():
        title = handler.getTitle()
        article = handler.getArticle()
        textAudio = handler.getAudio()
        if handler.isValid():
            return render_template('result.html', title=title, article=article)
        else:
            return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
