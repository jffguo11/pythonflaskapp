import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"


@app.route('/tuna')
def tuna():
    return "<h2> This is heading two </h2>"

@app.route('/apple', methods = ['GET', 'POST'])
def apple():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return 'You are proably using GET'


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile=html", name = name)

@app.route('/shopping')
def shopping():
    food = ['apple', 'banana', 'carrot', 'eggs']
    return render_template("shopping.html", food = food)

if __name__ == "__main__":
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))






