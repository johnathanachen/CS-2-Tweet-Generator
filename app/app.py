from flask import Flask, render_template
from dictogram import Dictogram
from markov_chain import Markov
from donald_scrape import Scrape

app = Flask(__name__)

file_name = "transcript.txt"
word_list = cleanup.clean_up_words_from_file(file_name)

@app.route('/')
def hello(random-tweet-text):
    return render_template("index.html", random-tweet-text=random-tweet-text)


if __name__ == '__main__':
    app.run(debug=True)
