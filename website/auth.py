import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
import flask
from . import db, mail
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message


auth = Blueprint("auth", __name__)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                sender='isv.siesgst@gmail.com',
                recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@auth.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return render_template("login.html", message="Invalid Password", user=current_user)
        else:
            return render_template("login.html", message="Email does not exist!", user=current_user)

    return render_template("login.html", user=current_user)



@auth.route("/signup/", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        fname = request.form.get("fname").capitalize()
        lname = request.form.get("lname").capitalize()
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        secret_access_key = request.form.get("secret-access")
        email_exists = User.query.filter_by(email=email).first()
    
        if email_exists:
            return render_template("register.html", message="Email already exists!", user=current_user)
        elif password1 != password2:
            return render_template("register.html", message="Password don't match!", user=current_user)
        elif secret_access_key != os.getenv("ISV_SECRET_ACCESS_KEY"):
            return render_template("register.html", message="Oppzz! Secret access key is incorrect!", user=current_user)
        else:
            new_user = User(email=email, fname=fname, lname=lname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)



@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))



@auth.route("/reset_password/", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            send_reset_email(user)
            flash('An email has been sent with instructions to reset your password. Do check your Spam folder if not found!', 'info')
            return redirect(url_for('auth.login'))
        else:
            return render_template("forgot-password.html", message="Account does not exist!")
    return render_template('forgot-password.html')



@auth.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('auth.reset_request'))
    else:
        if request.method == 'POST':
            password1 = request.form.get("password1")
            password2 = request.form.get("password2")
            if password1 != password2:
                return render_template("reset-password.html", message="Password don't match!")
            else:
                password = generate_password_hash(password1, method='sha256')
                user.password = password
                db.session.commit()
                return redirect(url_for('auth.login'))
    return render_template('reset-password.html')