import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from .views import views
# from .auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy()
db.init_app(app)

# app.register_blueprint(views, url_prefix="/")
# app.register_blueprint(auth, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))


@app.route('/')
def temperory():
    '''
    Add sample view function for default route
    '''
    return '''
    <html>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 15s ease infinite;
            }

            @keyframes gradient {
                0% {
                    background-position: 0% 50%;
                }

                50% {
                    background-position: 100% 50%;
                }

                100% {
                    background-position: 0% 50%;
                }
            }

            div.container {
                height: 50%;
                position: relative;
                margin: 0;
                position: absolute;
                top: 50%;
                left: 50%;
                margin-right: -50%;
                transform: translate(-50%, -50%)
            }

            div.container h1 h4 {
                font-size: 30px;
                color: white;
                margin: 0;
                position: absolute;
                font-family: Verdana, sans-serif;
                top: 50%;
                left: 50%;
                margin-right: -50%;
                transform: translate(-50%, -50%)
            }
        </style>

    </head>

    <body>
        <div class=container>
            <h1 style="color:white" align='center'>IEEE SIESGST Smart Village</h1>
            <h4 style="color:white" align='center'>Website under construction!!</h4>
        </div>

    </body>


    </html>
    '''

if __name__ == "__main__":
	app.run(port=os.getenv("PORT", default=5000))
