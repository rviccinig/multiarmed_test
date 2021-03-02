from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from multiarmed_test import User

#Registration form
class RegistrationForm(Flaskform):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('UserName',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords do not match!')])
    pass_confirm=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Register')

    # This method is doing a quary in our 'User' table in models.py , checking the 'email' field
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

        # This method is doing a quary in our 'User' table in models.py , checking the 'email' field
    def check_email(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')
