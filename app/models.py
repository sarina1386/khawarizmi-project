from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    uid = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(12), nullable=False, unique=True)
    password = db.Column(db.String(12), nullable=False)
    fname = db.Column(db.String(12), nullable=False)
    lname = db.Column(db.String(12), nullable=False)
    grade = db.Column(db.Integer, default=9)
    school = db.Column(db.String(30))
    score = db.Column(db.Integer, default=0)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Integer, default=1)
    seen_level = db.Column(db.String(100), default='[]')
    
    def get_id(self):
        return self.uid
    
    def __repr__(self):
        return f'User {self.uid} - {self.user_name}'


class Lessons(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, default=9)
    name = db.Column(db.String(25), nullable=False)
    image = db.Column(db.String(30), default="lesson-defualt")
    sections_num = db.Column(db.Integer, default=1)
    sections_intro = db.Column(db.String(500))

    def get_id(self):
        return self.lid
    
    def __repr__(self):
        return f'Lesson {self.lid} - {self.name}'


class Quiz(db.Model):
    qid = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, default=9)
    lesson = db.Column(db.Integer, default=1)
    lesson_id = db.Column(db.Integer, default=1)
    session = db.Column(db.Integer, default=1)
    questions = db.Column(db.String(5000), default='[]')
    answers = db.Column(db.String(1000), default='[]')
    time = db.Column(db.Integer, default=1)

    def get_id(self):
        return self.qid
    
    def __repr__(self):
        return f'Quiz {self.qid} - for lesson {self.lesson} and session {self.session}'
