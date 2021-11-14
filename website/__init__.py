import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
	app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
	app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
	mail.init_app(app)
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views)
	app.register_blueprint(auth)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		# since the id is just the primary key of our user table, use it in the query for the user
		return User.query.get(int(user_id))

	return app
