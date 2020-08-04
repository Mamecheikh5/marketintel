import os

from restodashboard import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    restodashboard.run()