from CLEANBLOG import  db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    post = db.relationship('Post', backref='user', lazy=True)

    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.name}, {self.email}'



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d'))
    post_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)


    def __init__(self,name, email, password):
        self.title = title
        self.subtitle = subtitle
        self.post_text = post_text

    def __repr__(self):
        return f'Post: {self.title}, {self.subtitle}'
    