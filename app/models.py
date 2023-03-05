from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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

    def get_id(self):
        return self.uid
    
    def __repr__(self):
        return f'User {self.uid} - {self.user_name}'




