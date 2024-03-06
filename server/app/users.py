from app import flask_app
from flask import Blueprint,request
from werkzeug.security import generate_password_hash
from Models.userModel import User
from database import db
user_bp  = Blueprint(
    'user', __name__, url_prefix='/api/user')

@user_bp.route('add_user',methods=['POST'])
def add_user():
    try:
        req_body = request.get_json()
        if req_body:
            Email = req_body.get('Email')
            UserName = req_body.get('username')
            password = req_body.get('password')
            hashed_password = generate_password_hash(password=password, method='sha256')
            user = User(Email=Email,UserName=UserName,Password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user.serialize()
        else:
            return "BAD REQUEST" ,400
    except BaseException as err:
        msg = f"Exception occured in add_user.{err}"
        print(msg)
        return msg,500
@user_bp.route('/login',methods=['POST'])
def login():
    try:
        pass
    except BaseException as err:
        pass