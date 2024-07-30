#!/usr/bin/rnv python3
"""Import required MOdu;e/Lib"""
from flask import Flask, render_template, request
fromflask_babel import Babel, _


app =Flask(__name__)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'


@label.localeselector
def get_locale():
    """REturn locale"""
    return request.args.get('lang', 'en')

@app.route('/')
def index():
    """return index"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
