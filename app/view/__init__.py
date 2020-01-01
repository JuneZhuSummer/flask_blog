from .index import index
from .user import user
from .upload import upload
from .collect import collect

# 蓝本配置

DEFAULT_BLUEPRINT = (
    # (蓝本,url前缀)
    (index, '/'),
    (upload, '/upload'),
    (user, '/user'),
    (collect, '/collect')
)


# 注册蓝本

def register_blueprints(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
