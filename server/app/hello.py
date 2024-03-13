from flask import Blueprint,jsonify
from app import flask_app
from flask_login import current_user
hello_bp  = Blueprint(
    'hello', __name__, url_prefix='/api/hello')

@hello_bp.route('/message')

def message():
    try:
        if current_user.is_authenticated:
            return jsonify({'message': f'Hello {current_user.UserName}'}), 200
        else:
            print("UnAuthorized login attempted on message API")
            return jsonify({'message': 'User are not authorzied to use this WebApp. Please login in order to use web app','error':"UNAUTHORIZED"}), 200
          
    except BaseException as err:
        msg = f"Exception occured in message API.{err}"
        print(msg)
        return msg
