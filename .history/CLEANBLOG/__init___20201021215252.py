from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_'] = False
app.config['MAIL_USERNAME'] = 'elvinyeka@gmail.com'
app.config['MAIL_PASSWORD'] = 'example'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)



from CLEANBLOG import  routes