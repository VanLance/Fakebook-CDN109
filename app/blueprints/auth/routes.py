from flask import render_template, flash, redirect
from . import bp as app
from app.forms import RegisterForm, SignInForm
from app.blueprints.social.models import User

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

@app.route('/register', methods=['GET',"POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        check_username = User.query.filter_by(username=username).first()
        check_email = User.query.filter_by(email=email).first()
        if check_username:
            flash(f'Username {username} is taken, enter different Username')
        elif check_email:
            flash(f'Email {email} already in use, enter new email')
        else:
            u = User(username=username,email=email,password_hash='')
            u.hash_password(password)
            print(u.password_hash)
            u.commit()

            flash(f'Register Requested for {email} {username}','success')
            return redirect('/')
    return render_template('register.jinja', form=form, title='Register')

@app.route('/signin', methods=['GET','POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.username} successfully signed in!')
        return redirect('/')
    return render_template('signin.jinja', sign_in_form=form)