import datetime

from application import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    person = db.relationship('Person')
