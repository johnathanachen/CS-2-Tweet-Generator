from flask import Flask, render_template
from cleanup import Clean
from markov import Markov

app = Flask(__name__)

file_name = "transcript.txt"
data = Clean().clean_text(file_name)

@app.route('/')
def hello():
    sentence = Markov().main(data, 10)
    return render_template("index.html", sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
