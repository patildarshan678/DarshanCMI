from flask import Flask
from database import db
from Models.userModel import User
flask_app = Flask(__name__)
environment_configuration = 'config.Developement'
flask_app.config.from_object(environment_configuration)
db.init_app(flask_app)
with flask_app.app_context():
    db.create_all() 
    db.session.commit()