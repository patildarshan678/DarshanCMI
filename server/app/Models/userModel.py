from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    UserName =  db.Column(db.String(100), nullable = False)
    Email =  db.Column(db.String(100), nullable = False)
    Password =  db.Column(db.String(500), nullable = False)
    def set_password(self,password):
        self.Password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.Password, password)

    def serialize(self):
        return{
            "UserName": self.UserName,
            "Email": self.Email
        }
    