from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/regions')
def regions():
    return 'Getting regions!'