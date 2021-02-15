from flask import render_template

from la_app import app

@app.route('/<name>')
def index(name):

    return render_template("index.html", nombre=name)
