from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def login():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(port=5000, debug=True)
