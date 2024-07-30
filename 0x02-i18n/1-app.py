#!/usr/bin/env python3
"""Import required Modul'Lib"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]

    def __init__(self):
        """Initialize the class"""
        pass
app.config.from_object(Config)

@app.route('/')
def index():
    """ return 1-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
