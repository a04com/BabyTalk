from flask import Flask, render_template
from parser import getNews  # Import the getNews function

app = Flask(__name__)

@app.route('/')
def home():
    news = getNews()  # Get the news from the parser
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)