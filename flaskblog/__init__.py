from flask import Flask
from flask_sqlalchemy import SQLAlchemy #First 'pip install flask-sqlalchemy'


app=Flask(__name__)
app.config['SECRET_KEY'] = "01a1a9534fbb91fb97639be1074f774f" #python random number generator??
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes