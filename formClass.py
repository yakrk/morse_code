from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class MorseCodeForm(FlaskForm):
    input_text = StringField('Text  ', validators=[DataRequired()])
    submit = SubmitField('Convert')