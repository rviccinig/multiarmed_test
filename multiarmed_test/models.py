# The models file is the database models

# Here I am importing fro from puppycompanyblog/__init__.py
from puppycompanyblog import  db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import datetime import datetime

#Now I can create the databases and register the blueprints

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #Its a string because it is goung to be a link. The size limit 64 is arbitraru, index=True has to do with SQL  you can use the column later    email = db.Column(db.String(64), unique=True, index=True)
    usename = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password)
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"
