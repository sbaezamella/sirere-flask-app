import subprocess
import sys
from os.path import dirname, join

from dotenv import load_dotenv
from flask_script import Manager, Server

from sirere import create_app

# Load .env with environment vars
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


manager = Manager(create_app)

manager.add_command('runserver', Server(host='localhost'))


@manager.command
def isort():
    """Runs isort."""
    _sorted = subprocess.call(['isort',
                               '--gitignore',
                               '.',
                               ]) == 0
    if _sorted:
        print('OK')
    sys.exit(_sorted)


@manager.command
def lint():
    """Runs code linter."""
    linted = subprocess.call(['pylint',
                              'sirere/',
                              'manage.py',
                              '--rcfile=.pylintrc',
                              ]) == 0
    sys.exit(linted)


if __name__ == '__main__':
    manager.run()
