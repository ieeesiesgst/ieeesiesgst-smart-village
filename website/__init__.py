import os
from flask import Flask
from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix="/")
	app.register_blueprint(auth, url_prefix="/")

	from .models import User, Post

	db.create_all(app=app)

	login_manager = LoginManager()
	login_manager.login_view = "auth.login"
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(user_id):
		return UserMixin.query.get(int(user_id))

	return app
