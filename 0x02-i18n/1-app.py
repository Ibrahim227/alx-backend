#!/usr/bin/env python3
"""Import required Modul'Lib"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_pyfile('babel.cfg')
babel = Babel(app)


@app.route('/')
def index();
    """ return 1-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
