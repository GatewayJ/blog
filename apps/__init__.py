from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps.member_center import member_center
from apps.error_handler import error_handlers
from config import config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['dev'])
    config['dev'].__init__(app)
    db.__init__(app)
    migrate = Migrate(app, db)

    app.register_blueprint(member_center)
    app.register_blueprint(error_handlers)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return manager
