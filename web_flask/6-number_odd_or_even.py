#!/usr/bin/python3
""" Script that starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    """ Display “Python ”, followed by the value of the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:number>')
def only_num(number):
    """ Display only if is number
    """
    return '{} is a number'.format(number)


@app.route('/number_template/<int:number>')
def num_template(number):
    """ Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ Display a HTML page only if n is an integer
    """
    if (n % 2 == 0):
        result = "even"
    else:
        result = "odd"

    return render_template('6-number_odd_or_even.html', n=n, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
