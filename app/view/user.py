"""
用户模块
"""
from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/')
def index():
    return "这是个人中心"
