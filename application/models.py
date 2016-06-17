import datetime
from application import db


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(60))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Person {}>".format(self.id)

