from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Appointment, Doctor, Patient
from app.forms import AppointmentForm

@app.route('/schedule', methods=['GET', 'POST'])
def schedule_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            patient_id=form.patient.data.id,
            doctor_id=form.doctor.data.id,
            date=form.date.data,
            confirmed=True
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Cita agendada correctamente.', 'success')
        return redirect(url_for('appointment_list'))
    return render_template('appointment_form.html', form=form)

@app.route('/cancel/<int:appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    appointment.confirmed = False
    db.session.commit()
    flash('Cita cancelada correctamente.', 'info')
    return redirect(url_for('appointment_list'))

@app.route('/doctor/<int:doctor_id>/availability', methods=['POST'])
def update_availability(doctor_id):
    # Lógica para actualizar la disponibilidad del médico
    pass
