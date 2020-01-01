"""
用户模型
"""

from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    icon = db.Column(db.String(64), default='default.jpg')
    phone = db.Column(db.INTEGER(), unique=True)
    email = db.Column(db.String(128), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(64))


