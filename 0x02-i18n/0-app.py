#!/usr/bin/env python3
"""Import REquired Module/Lib"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """return 0-index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
