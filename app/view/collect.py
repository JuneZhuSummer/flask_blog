"""
收藏模块
"""
from flask import Blueprint

collect = Blueprint('collect', __name__)


@collect.route('/')
def index():
    return "这是收藏页面"
