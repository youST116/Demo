from datetime import datetime
#from flask import url_for
from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class Customer(db.Model):
    customer_address = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128),nullable=False)

    appointment = db.relationship('Appointment', back_populates='Customer')

    def _init(self, customer_address, first_name, last_name):
        self.customer_address = customer_address
        self.first_name = first_name
        self.last_name = last_name

    def _repr_(self):
        return (f'<Customer{self.first_name} {self.last_name}>')
