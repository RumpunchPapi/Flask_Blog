from flask import Flask
from flask_sqlalchemy import SQLAlchemy #First 'pip install flask-sqlalchemy'
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app=Flask(__name__)
app.config['SECRET_KEY'] = "01a1a9534fbb91fb97639be1074f774f" #python random number generator??
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' # customises flashed message to nicer bootstrap class

from flaskblog import routes