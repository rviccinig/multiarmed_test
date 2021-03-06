#############3 Creating App #####################
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)

############# Configuration ####################
app.config['SECRET_KEY'] = 'mysecretkey'


############## Database Setup ##########
#Very importnat to check the paths for the database!!
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://'+os.path.join(basedir,'/data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

############# Blueprints ###################################
# this is where the Blueprints of the application that render the views are set up
from multiarmed_test.core.views import users_blueprint

app.register_blueprint(users_blueprint,url_prefix="/")
