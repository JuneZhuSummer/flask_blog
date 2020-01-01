"""
用户模块
"""
from flask import Blueprint, render_template
from ..models.user import User
from ..extensions import db

user = Blueprint('user', __name__)
user_m = User()


# 主页控制器
@user.route('/')
def index():
    return "用户主页"


@user.route('/login')
def login():
    return render_template("user/login.html")

