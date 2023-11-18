from flask import Flask
from flask import render_template

"""
Author: Lns-XueFeng
Create Time: 2023.11.11
Python Version: 3.9
"""


__author__ = "Lns-XueFeng"
__version__ = "0.1"
__license__ = "MIT"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("piano.html")


if __name__ == "__main__":
    app.run(debug=True)
