# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
#This one imports the __init__.py file automatically
from multiarmed_test import db
from multiarmed_test.models import User
from multiarmed_test.core.forms import RegistrationForm

users_blueprint = Blueprint('users', __name__)

# register a users


@users_blueprint.route('/', methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('thanks for registration!')
        return redirect(url_for('thankyou.html'))
    return render_template('signup1.html',form=form)
