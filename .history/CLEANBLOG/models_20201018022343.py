from CLEANBLOG import  db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)