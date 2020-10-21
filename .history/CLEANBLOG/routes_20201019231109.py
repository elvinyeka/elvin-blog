from flask import render_template, flash, redirect, url_for, abort
from CLEANBLOG import app, db
from CLEANBLOG.forms import RegisterForm, LoginForm, PostForm
from CLEANBLOG.models import  User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', title = 'HOME', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title = 'ABOUT')


@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'CONTACT')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.name.data} registered', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'REGISTER', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.password== form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash(f'Login Unseccsful', 'danger')
    return render_template('login.html', title = 'LOGIN', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/post.new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post= Post(title=form.title.data, subtitle= form.subtitle.data, post_text= form.post_text.data, user= current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Post is created', 'succes')
        return redirect(url_for('index'))
    return render_template('create_post.html', title = 'Create Post', form=form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = 'post.title', post=post)

@app.route('/post/<int:post_id>/edit')
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = PostForm()