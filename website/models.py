from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    birthday = db.Column(db.Integer)
    password = db.Column(db.String(150))


class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(300))
    author = db.Column(db.String(150))
    new_date = db.Column(db.String(150))
    content = db.Column(db.String())
    category = db.relationship('Category', backref='news')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_title = db.Column(db.String(300))
    new_id = db.Column(db.Integer, db.ForeignKey('news.id'))

