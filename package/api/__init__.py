from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from package.models.user import User
from package import db

api = Blueprint('api', __name__, url_prefix='/api')

@api.post('/signup')
def signup():
    body = request.get_json()
    name = body.get('name')
    password = body.get('password')

    user = User.query.filter_by(username=name).first() 

    if user: 
        return 'User already exists', 409

    
    new_user = User(username=name, password=generate_password_hash(password, method='sha256'), usertoken=generate_password_hash(name, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return 'User created successfully', 201

@api.post('/login')
def login():
    body = request.get_json()
    name = body.get('name')
    password = body.get('password')

    user = User.query.filter_by(username=name).first()

    if not user or not check_password_hash(user.password, password):
        return 'Invalid credentials', 401
        
    return 'Login successful', 200

