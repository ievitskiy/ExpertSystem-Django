from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_quest = db.Column(db.String(64), default="")
    second_quest = db.Column(db.String(64), default="")
    first_quest_complete = db.Column(db.Boolean, default=False)
    second_quest_complete = db.Column(db.Boolean, default=False)
    quest_pos = db.Column(db.String(8), default='0')
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Quests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ind = db.Column(db.String(16))
    quest = db.Column(db.String(64))

    def __repr__(self):
        return '<ind {}, quest {}>'.format(self.ind, self.quest)


@login.user_loader
def load_user(us_id):
    return User.query.get(int(us_id))
