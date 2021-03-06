from flask import render_template, flash, redirect, url_for
from CLEANBLOG import app
from CLEANBLOG.forms import RegisterForm, LoginForm


@app.route('/')
def index():
    return render_template('index.html', title = 'HOME')

@app.route('/about')
def about():
    return render_template('about.html',title = 'ABOUT')

@app.route('/post')
def post():
    return render_template('post.html', title = 'POST')

@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'CONTACT')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'{form.name.data} registered', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title = 'REGISTER', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    if form.email.data == 'elvinyeka@gmail.com':
            flash(f' Giriş uğurlu oldu', 'success')
            return redirect(url_for('index'))
    return render_template('login.html', title = 'LOGIN', form=form)