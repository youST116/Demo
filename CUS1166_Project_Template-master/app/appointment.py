class Appointment(db.Model):
    title = db.Column(db.String(128), index=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    starting_time_duration = db.Column(db.DateTime, nullable=False)
    ending_time_duration = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(5000), index=True)

    def _init_(self, title, date, starting_time_duration, ending_time_duration, notes)
        self.title = title
        self.date = datetime
        self.starting_time_duration = starting_time_duration
        self.ending_time_duration = ending_time_duration
        self.notes = notes

    def _repr_(self):
        return (f'<Appointment {self.customer} @ {self.start}>')
        
