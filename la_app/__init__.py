from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersegura'

from la_app import routes