from datetime import datetime
from . import db
from flask_login import UserMixin # type: ignore


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


# def __init__(self, username, email):
#     self.username = username
#     self.email = email


class Biodata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    regno = db.Column(db.String(20))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    email = db.Column(db.String(150))
    mobilenumber = db.Column(db.String(15))
    address = db.Column(db.String(255))
    department = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Activitycategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Occurrence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_range = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    occurrence_id = db.Column(db.Integer, db.ForeignKey('occurrence.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('activitycategory.id'))
    duration = db.Column(db.Integer)  # Assuming duration is in minutes
    total_participants = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    duration = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


