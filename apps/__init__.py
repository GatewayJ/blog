from flask import Flask

import logging.config
from flask_sqlalchemy import SQLAlchemy
from config import config
from log_config import LOGGING_DIC
from flask_jwt_extended import JWTManager

logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger('root')
db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_type='dev'):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    config['dev'].__init__(app)

    jwt.__init__(app)
    db.__init__(app)

    from apps.member_center import member_center
    from apps.error_handler import error_handlers
    app.register_blueprint(member_center)
    app.register_blueprint(error_handlers)
    return app
