from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


db = SQLAlchemy()


def create_app(config_type='dev'):
    from apps.member_center import member_center
    from apps.error_handler import error_handlers
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    config['dev'].__init__(app)
    db.__init__(app)

    app.register_blueprint(member_center)
    app.register_blueprint(error_handlers)
    return app
