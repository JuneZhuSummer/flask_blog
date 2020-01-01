"""
页面蓝本创建
"""


from .main import main
from .user import user
from .upload import upload
from .collect import collect
from .admin.backstage import backstage
from .admin.push import push

# 蓝本配置

DEFAULT_BLUEPRINT = {
    # (蓝本,url前缀)
    main: '/',
    user: '/user/',
    upload: '/upload',
    collect: '/collect',
    backstage: '/admin/',
    push: '/admin/push'
}


# 注册蓝本
def register_blueprints(app):
    for key in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint=key, url_prefix=DEFAULT_BLUEPRINT[key])
