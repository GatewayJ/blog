# coding:utf-8
# author:JiHW


class Config():
    SECRET_KEY = 'sd340y30t8jdfjsdkg-q'
    JWT_SECRET_KEY = SECRET_KEY
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    @staticmethod
    def __init__(self):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/user'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


config = {
    "dev": DevelopmentConfig
}
