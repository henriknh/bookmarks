from flask import Blueprint, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash # http://flask.pocoo.org/snippets/54/
import db as db

user = Blueprint('user', __name__)

@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['email'],
                request.form['password']):
            session['id'] = db.getUserWithEmail(request.form['email'])['id']
    return redirect(url_for('index'))

@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if valid_register(request.form['email'], request.form['password1'],
                request.form['password2']):
            db.insertUser(request.form['email'], password_hash(request.form['password1']))
            session['id'] = db.getUserWithEmail(request.form['email'])['id']
    return redirect(url_for('index'))

@user.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('index'))

def valid_login(email, password):
    valid = True
    if email is "":
        flash("Email can't be empty")
        valid = False
    if password is "":
        flash("Password can't be empty")
        valid = False
    if not user_exists(email):
        flash("No user with that email is registered")
        valid = False
        return valid
    if not password_match(email, password):
        flash("Invalid password")
        valid = False
    return valid

def valid_register(email, password1, password2):
    valid = True
    if email is "":
        flash("Email can't be empty")
        valid = False
    if password1 is "":
        flash("Password can't be empty")
        valid = False
    if user_exists(email):
        flash("Email already registered")
        valid = False
    if password1 != password2:
        flash("Passwords does not match")
        valid = False
    return valid

def user_exists(email):
    return db.getUserWithEmail(email)

def password_match(email, password):

    user = db.getUserWithEmail(email)

    if not user:
        return False
    else:
        print(db.getUserWithEmail(email)['password'])
        print(check_password_hash(db.getUserWithEmail(email)['password'], password))
        return check_password_hash(db.getUserWithEmail(email)['password'], password)

def password_hash(password):
    return generate_password_hash(password)
