from datetime import timedelta
class Constants(object):
    Debug = False
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///FlaskDatabase.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:abc123@127.0.0.1:5432/CMITest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'SECT_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(45)
    
class Developement(Constants):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'SECRET_KEY_DEV'