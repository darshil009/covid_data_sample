from app import db
from flask_login import UserMixin


class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)

    def __init__(self, name, email, password, state):
        self.name = name
        self.email = email
        self.password = password
        self.state = state