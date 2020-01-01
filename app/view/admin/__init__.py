from .index import index
from .push import push

# 蓝本配置

DEFAULT_BLUEPRINT = (
    # (蓝本,url前缀)
    (index, '/admin/'),
    (push, '/admin/push'),
)


# 注册蓝本

def register_blueprints(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
