import datetime
import sqlalchemy as db
from application.database import Base
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(60))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Person {}>'.format(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Post(Base):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    person = relationship(Person)
