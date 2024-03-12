from app import flask_app
def register_bp():
     from hello import hello_bp
     from users import user_bp
     from file import files_bp
     flask_app.register_blueprint(user_bp)
     flask_app.register_blueprint(hello_bp)
     flask_app.register_blueprint(files_bp)
register_bp()
if __name__ == '__main__':
     
     flask_app.run(host='0.0.0.0', port=5000,debug=True) 