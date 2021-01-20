#!/usr/bin/python3
""" Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Say hello

    Returns:
        [str]: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def diplay_hbnb():
    """ Display 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Display “C ” followed by the value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/(<text>)')
def python_is_cool(text="is cool"):
    """ Display “Python ”, followed by the value of the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
