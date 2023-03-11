from . import bp as app
from flask import Flask, render_template

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