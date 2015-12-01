#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand

from rodeo.app import create_app
from rodeo.config import DefaultConfig
from rodeo.extensions import db


app = create_app(DefaultConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, and db by default.
    """
    return {'app': app, 'db': db}


@manager.command
def test():
    """Run the tests."""
    import nose
    return nose.main()

manager.add_command('runserver', Server(port=5401))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
