from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate()


# 让扩展初始化   也就是 跟app绑定

def config_extensions(app):
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
