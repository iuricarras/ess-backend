from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000), unique=True)
    usertoken = db.Column(db.String(100), unique=True)
