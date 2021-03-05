# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
#This one imports the __init__.py file automatically
from multiarmed_test import db
from multiarmed_test.models import User
from multiarmed_test.core.forms import RegistrationForm
import numpy as np

users_blueprint = Blueprint('users', __name__)

# function that displays a random page depending on the probability
templates=['Shopify_sign_in_1.html','Shopify_sign_in_2.html','Shopify_sign_in_3.html']
prob=[0.34,0.34,0.32]


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
    choice=np.random.choice(templates,1,p=prob)[0]
#choice is an array that produces the path for one of the html but I scope the 0 element.
    return render_template(choice,form=form)
