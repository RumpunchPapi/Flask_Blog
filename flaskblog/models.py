from datetime import datetime
from sqlalchemy.orm import backref
from flaskblog import db


class User(db.Model): # the table name automatically set to 'user', however this can be chenged
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) #backref creates 'author' column for every user who creates a posts;
                                                                 # this is not actully a column but a query in the background that links the two tables. lazy means SQLAlchemy will load the data into the db in one go as neccessary  

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# To craete the tables and data base, go to the terminal run python in project directory: 'from flaskblog import db' then 'db.create_all()'
# db.session.add(admin), db.session.add(guest), db.session.commit(); User.query.all(); db.drop_all() = deletes all table and rows

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

