"""
上传模块
"""
from flask import Blueprint

upload = Blueprint('upload', __name__)


@upload.route('/')
def index():
    return "这是上传页面"
