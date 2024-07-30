#!/usr/bin/env python3
"""Import REquired Module/Lib"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return0-index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
