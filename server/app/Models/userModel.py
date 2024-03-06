from database import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)   
    UserName =  db.Column(db.String(100), nullable = False)
    Email =  db.Column(db.String(100), nullable = False)
    Password =  db.Column(db.String(100), nullable = False)
    def __init__(self,UserName,Email,Password):
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
    def serialize(self):
        return{
            "UserName": self.UserName,
            "Email": self.Email
        }
    