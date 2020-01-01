"""
主页
"""
from flask import Blueprint

backstage = Blueprint('backstage', __name__)


@backstage.route('/')
def index():
    return "这是管理员主页"
