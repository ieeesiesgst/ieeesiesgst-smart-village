import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .views import views
# from .auth import auth

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
	db.init_app(app)

	app.register_blueprint(views, url_prefix="/")
	# app.register_blueprint(auth, url_prefix="/")
		
	login_manager = LoginManager()
	login_manager.login_view = "auth.login"
	login_manager.init_app(app)

	# @login_manager.user_loader
	# def load_user(id):
	#     return User.query.get(int(id))

	return app



