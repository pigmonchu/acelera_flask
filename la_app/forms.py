from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from la_maquina.entities import rotor_types, reflector_types, abecedario

def ismyAlph(formulario, campo):
    for caracter in campo.data:
        if caracter not in abecedario:
            raise ValidationError ("Mensaje de entrada con caracteres no permitidos")


class EnigmaForm(FlaskForm):
    texto_entrada = StringField("Input", validators=[DataRequired("Campo requerido"), ismyAlph])
    texto_salida = StringField("Output")

    rotor1 = SelectField("Rotor 1", choices=list(rotor_types), validators=[DataRequired()])
    rotor1_ini = SelectField("Pos", choices=list(abecedario))

    reflector = SelectField("Reflector", choices=list(reflector_types), validators=[DataRequired()])

    aceptar = SubmitField("Codificar")