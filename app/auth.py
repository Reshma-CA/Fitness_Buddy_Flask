from flask import Blueprint, render_template,request,redirect,url_for

from werkzeug.security import generate_password_hash
from . model import User
from . import db
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

    print(name, email, password, repassword)

    return redirect(url_for('auth.login'))
    

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_user():
    name = request.form.get('username')
    password = request.form.get('password')

    print(name,password)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
def logout():
    return "logout"