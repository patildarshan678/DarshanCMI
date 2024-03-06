from datetime import timedelta
class Constants(object):
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///FlaskDatabase.db'
    JWT_SECRET_KEY = 'SECT_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(45)
    
class Developement(Constants):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'SECRET_KEY_DEV'