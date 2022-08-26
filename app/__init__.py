from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    source = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(120))
    urlToImage = db.Column(db.String(255))
    publishedAt = db.Column(db.String(120))
    content = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %r>' % self.url

    def get_id(self):
        return self.id

    def convert_to_dict(self):
        post = {
            'id': self.id,
            'source': self.source,
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'urlToImage': self.urlToImage,
            'publishedAt': self.publishedAt,
            'content': self.content,
        }
        return post


db.create_all()

from app import views
