from flask import Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>HELLO KAATRU TEAM!!!</h1>'
