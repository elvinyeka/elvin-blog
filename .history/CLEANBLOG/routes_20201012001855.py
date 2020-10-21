from flask import render_template
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