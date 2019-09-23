from apps import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)
    manager = Manager(app)
    from apps.member_center.models import user
    print(user.AdminUser)
    manager.add_command('db', MigrateCommand)
    manager.run()
