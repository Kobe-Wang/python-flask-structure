# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from flask import jsonify

app = create_app(os.getenv('APP_SETTINGS') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)

manager.add_command('db', MigrateCommand)

@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import sys
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
    sys.exit(not test_result.wasSuccessful())

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade

    # migrate database to latest revision
    upgrade()


if __name__ == '__main__':
    manager.run()