#!/usr/bin/env python3
"""Import required Modul'Lib"""
from flask import Flask, render_template
from flask_babel import Babel


# app = Flask(__name__)
# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
# babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index() -> str:
    """ return 1-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
