import firebase_admin
from firebase_admin import auth, credentials

from cryptography.fernet import Fernet
from flask import Flask, redirect, url_for, session, request
from flask import render_template

import os

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

app.secret_key = Fernet.generate_key()

@app.route('/')
def index():
    """
    If the user is already signed in, then redirect user to
    the profile page. If not, redirect user to the sign in page
    """
    page = 'login' if 'user' not in session else 'profile'
    return redirect(url_for(page))


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = session['user'] if 'user' in session else None
    if request.method == 'GET':
        print(session)
        if user:
            return redirect(url_for('index'))
        else:
            return render_template('index.html')
    if request.method == 'POST':
        data = request.json
        print(data["user"])
        session['user'] = data["user"]
        return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('logout.html')


app.run(port=5000, debug=True)
