from flask import Flask
from zappa.asynchronous import run

from moola.core import test_log

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    name = test_log()
    return f"Hi {name}"
