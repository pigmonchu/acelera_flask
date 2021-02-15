from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola, mundo!'

@app.route('/adiosito')
def goodbye():
    return 'adios mundo cruel'