# The models file is the database models

# Here I am importing fro from puppycompanyblog/__init__.py
from multiarmed_test import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

#Now I can create the databases and register the blueprints

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(64), unique=True, index=True)
    landing_page=db.Column(db.string(64))

    def __init__(self, email):
        self.email = email
        self.landing_page=landing_page

    def __repr__(self):
        return f"Email{self.email}"
