from flask import Flask, render_template, request 
import requests
from translate import translate_work

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    url = request.form['url']
    text = translate_work(url)
    return render_template('result.html', text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    