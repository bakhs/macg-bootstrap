import pyrebase
from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

firebase_config = {
    "apiKey": "AIzaSyAtl204Z-7BI3KHjlk3XtU7ivP8PaO5Jr4",
    "authDomain": "dj-site-3b616.firebaseapp.com",
    "databaseURL": "https://dj-site-3b616.firebaseio.com",
    "storageBucket": "dj-site-3b616.appspot.com",
    "messagingSenderId": "943029467573",
}

firebase = pyrebase.initialize_app(firebase_config)


@app.route('/')
def index():
    """
    If the user is already signed in, then 
    redirect user to the profile page

    If not, redirect user to the sign in page
    """
    print(firebase.auth().current_user)
    if not firebase.auth().current_user:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('profile'))


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    # TODO: Find better way to logout a user
    return render_template('logout.html')


app.run(port=5000, debug=True)
