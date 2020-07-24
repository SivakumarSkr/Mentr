import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Skill(db.Model):
    __tablename__ = 'skill'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    followers_count = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.followers_count = 0

    def __repr__(self):
        return f'<id {self.id} - {self.name}>'


skills = db.Table('skills',
                  db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True),
                  db.Column('mentor_id', db.Integer, db.ForeignKey('mentor.id'), primary_key=True)
                  )


class User(db.Model):
    __tablename__ = 'User'
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    firs_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=False, unique=True, index=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_join = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email = db.Column(db.String(100), nullable=True, unique=True, index=True)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Mentor(User):
    __tablename__ = 'mentor'
    is_prime = db.Column(db.Boolean, default=False)
    skills = db.relationship('Skill', secondary=skills, lazy='subquery', backref=db.backref('mentors', lazy=True))

    def __repr__(self):
        return f'<Mentor : {self.username}>'


class Student(User):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
