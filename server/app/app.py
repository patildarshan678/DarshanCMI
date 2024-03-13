from flask import Flask
from database import db
from Models.userModel import User
from flask_cors import CORS
from Models.csvModels import CSVData
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

flask_app = Flask(__name__)
environment_configuration = 'config.Developement'
flask_app.config.from_object(environment_configuration)
CORS(flask_app,origins=['http://localhost:3000'])
db.init_app(flask_app)
login_manager = LoginManager()
login_manager.init_app(flask_app)

@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))

with flask_app.app_context():
    db.create_all() 
    db.session.commit()