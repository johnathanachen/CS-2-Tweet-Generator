from flask import Flask
import cleanup
import tokenize
import word_count
import sample
import sentence

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello the name is Johno and I love to ing and dance"


if __name__ == '__main__':
    app.run(debug=True)
