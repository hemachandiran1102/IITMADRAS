from flask import Flask

app = Flask(__name__)


app.logger.disabled = True
    log = logging.getLogger('werkzeug')
    log.disabled = True
    logging.getLogger('werkzeug').disabled = True
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'
