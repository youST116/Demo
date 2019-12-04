from flask import render_template,  redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Task
from datetime import datetime

@dp.route('/', methods = {"GET", "POST"})
def app_index():
    return render_template(main/app_index.html)


@dp.route('/recordappointmentlist/<int:appointment_id>', methods = {'GET', 'POST'})
def record_list(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        current_appointment.title = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.date = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.starting_time_duration = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.ending_time_duration = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.notes = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        db.session.add(current_appointment)
        db.session.commit()

        return redirect(url_for(main.record_list.html))
        record_list = db.session.query(Appointment).all()

        return render_template('main/record_list.html', record_list=record_list, form=form)

@dp.route('/get_appointment/<int: appointment_id>', methods = {"GET", "POST"})
def get_appointment(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit()
        current_appointment=Appointment.query.filter_by(apointment_id=appointment_id).first_or_404()

        return redirect(url_for(main.get_appointment.html))
        get_appointment = db.session.query(Appointment).all()

        return render_template("main/get_appointment.html", get_appointment=get_appointment,form=form)
