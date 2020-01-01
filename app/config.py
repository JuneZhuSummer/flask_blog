
class Config:
    # 配置数据库
    # ORM模型
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:5201314@localhost:3306/flask_blog'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:5201314@localhost:3306/flask_blog'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:5201314@localhost:3306/flask_blog'


config = {
    'develop': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
