from flask_mail import Message
from app import mail

def send_confirmation_email(patient_email, appointment_details):
    msg = Message('Confirmación de Cita', recipients=[patient_email])
    msg.body = f'Tu cita ha sido confirmada para {appointment_details}.'
    mail.send(msg)
