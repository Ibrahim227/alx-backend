#!/usr/bin/env python3
"""Import required Modul'Lib"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@label.selector
def get_locale():
    """selct and return lang"""
    return request.accept_languages.best_match(['en', 'de', 'fr'])

@app.route('/')
def index() -> str:
    """ return 1-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
