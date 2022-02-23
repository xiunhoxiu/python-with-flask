from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)  
        # func: gets the current date and time and store in the DateTime field

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
        # associate different info with different users via a foreign key
        # foreign key (column): always ref an ID of another db.Column
        # one to many, many to one, one to one: look up Flask SQLalchemy documentation
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  
        # uniquely identify an object - primary key = unique identifier (typically an integer)

    email = db.Column(db.String(150), unique=True) 
        # max length of character, email is unique
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
