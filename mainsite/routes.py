from flask import render_template, url_for, flash, redirect, request
from mainsite import app, db, bcrypt
from mainsite.forms import  LoginForm, RegistrationForm
from mainsite.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


# userlist = {
#     "admin" : {
#         "name": "admin",
#         "password": "Password@123"
#     },
# }



@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    # if form.validate_on_submit():
        # user = User.query.filter_by(email=form.username.data).first()
    print(form.username.data)
    if "admin" == "admin" and "admin" == "admin" :
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/moodle")
def moodel():
    return render_template('moodle.html')

@app.route("/zimbra")
def zimbra():
    return render_template('zimbra.html')

@app.route("/punch")
def punch():
    return render_template('punch.html')

