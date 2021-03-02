#############3 Creating App #####################
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)

##############Database Setup##########

basedir=os.path.abspath(os.path.dirname(__file___))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://'+os.path.join(basicdir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)


#############Login Configurations################
# We are going to register a Blueprint called users attached to to the login view

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'
