# coding:utf-8
# author:JiHW

class Config():
    SECRET_KEY = 'sd340y30t8jdfjsdkg-q'

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