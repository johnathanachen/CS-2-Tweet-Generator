from flask import Flask, render_template
from sampling import *
from histo_dict import *

app = Flask(__name__)

@app.route("/")
def hello():
    print(run_sampling())
    # return run_sampling()

if __name__ == '__main__':
    app.run(debug=True)
