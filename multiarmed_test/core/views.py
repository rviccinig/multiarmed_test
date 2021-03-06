# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
#This one imports the __init__.py file automatically
from multiarmed_test import db
from multiarmed_test.models import User
from multiarmed_test.core.forms import RegistrationForm
import numpy as np

users_blueprint = Blueprint('users', __name__)
thank_you_blueprint=Blueprint('thankyou',__name__)

# function that displays a random page depending on the probability
templates=['Shopify_sign_in_1.html','Shopify_sign_in_2.html','Shopify_sign_in_3.html']
prob=[0.34,0.34,0.32]


# register a users
@users_blueprint.route('/', methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    choice=np.random.choice(templates,1,p=prob)[0]
    #choice is an array that produces the path for one of the html but I scope the 0 element.
    if form.validate_on_submit():
        user = User(email=form.email.data,landing_page=choice)
        db.session.add(user)
        db.session.commit()
        #This "thankyou" is the name I gave it in my blueprint!!!!!! and then thanks is the function!
        return redirect(url_for('thankyou.thanks'))
    return render_template(choice,form=form)

# Route to Thanks page.
@thank_you_blueprint.route('/thankyou',methods=['GET', "POST"])
def thanks():
    return render_template('thankyou.html')
