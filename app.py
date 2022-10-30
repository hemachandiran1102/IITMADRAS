from flask import Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    return send_from_directory('test','index.html') 
