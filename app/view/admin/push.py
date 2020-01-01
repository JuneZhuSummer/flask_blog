"""
推送
"""
from flask import Blueprint

push = Blueprint('push', __name__)


@push.route('/')
def index():
    return "这是推送页面"
