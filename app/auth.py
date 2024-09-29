from flask import Blueprint, render_template, request, redirect, url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_user():
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    repassword = request.form.get('repassword')

    user = User.query.filter_by(name=name).first()
    if user:
        flash("User already exists")
        return redirect(url_for('auth.signup'))

    new_user = User(
        name=name, 
        email=email, 
        password=generate_password_hash(password, method="pbkdf2:sha256"),
        repassword=generate_password_hash(repassword, method="pbkdf2:sha256")
    )
    db.session.add(new_user)
    db.session.commit()

    flash("Signup successful")
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def handle_login():
    name = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()

    if not user or not check_password_hash(user.password, password):
        flash("Invalid credentials")
        return redirect(url_for('auth.login'))
    
    login_user(user)  # Log in the user
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Use logout_user instead of login_user
    return redirect(url_for('main.index'))
