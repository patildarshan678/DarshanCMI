from app import flask_app
from flask import Blueprint,request,jsonify
from Models.userModel import User
from werkzeug.security import check_password_hash
from flask_login import login_user,logout_user,current_user
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
            user = User()
            user.Email = Email
            user.set_password(password=password)
            user.UserName = UserName
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
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        db_user = User.query.filter_by(UserName=username).first()
        if db_user and check_password_hash(db_user.Password, password):
            if current_user.is_authenticated== False:
                login_user(db_user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password','error':'UnAthorized'}), 200

    except BaseException as err:
        msg = f"Exception occured in login API. {err}"
        print(msg)
        return msg , 500
@user_bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200