#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """function that returns a text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """function that returns a text variable"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)