from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
def index():
    cdn={
        'instructors':('lucas','dylan'),
        'students':['blane','ashmika','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.jinja', form=form)