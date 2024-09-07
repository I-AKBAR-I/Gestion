from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    patient = SelectField('Paciente', validators=[DataRequired()])
    doctor = SelectField('Doctor', validators=[DataRequired()])
    date = DateTimeField('Fecha y Hora', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    submit = SubmitField('Agendar Cita')
