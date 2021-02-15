from flask import render_template, request, flash

from la_app import app
from la_app.forms import EnigmaForm

from la_maquina.entities import Enigma, Rotor, Reflector, rotor_types, reflector_types, abecedario

def_rotor = Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
def_reflector = Reflector(reflector_types['D'])
enigma = Enigma([def_rotor], def_reflector)

@app.route('/', methods=['GET', 'POST'])
def index():

    form = EnigmaForm()
    if request.method == 'POST':
        if form.validate():
            enigma.rotores = [Rotor(abecedario, rotor_types[form.rotor1.data][0], rotor_types[form.rotor1.data][1])]
            enigma.reflector = Reflector(reflector_types[form.reflector.data])
            enigma.ini = form.rotor1_ini.data

            try:
                output = enigma.codifica(form.texto_entrada.data)
            except ValueError as e:
                print("Error al codificar", e)
                flash("Codigo de entraada invalido")
                output = ""

            form.texto_salida.data = output
            form.rotor1_ini.data = enigma.ini

    return render_template("index.html", formulario=form)

    