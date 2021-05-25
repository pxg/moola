from flask import Flask
from zappa.asynchronous import run

from moola.core import test_log
from moola.shell import get_monzo_balance

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return f"Hi Monzo user!"
