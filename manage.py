from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def load_fixtures():
    """
    Loads database fixtures
    """
    import glob
    from flask_fixtures.loaders import YAMLLoader
    from flask_fixtures import load_fixtures

    db.drop_all()
    db.create_all()

    for fixture_dir in app.config.get('FIXTURES_DIRS', ['./fixtures/']):
        for fixture_file in glob.glob(fixture_dir + '/*.yml'):
            fixtures = YAMLLoader().load(fixture_file)
            load_fixtures(db, fixtures)


if __name__ == '__main__':
    manager.run()
