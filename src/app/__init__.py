"""
Flask application fabric module
"""

from flask import Flask

import logging
from logging.handlers import RotatingFileHandler
import os

from .config import Config
from .bot import Bot
from .telegram import TelegramBotManager


def create_app():
    """
    Flask application fabric
    :return: Flask instance
    :rtype: flask.Flask
    """
    app = Flask(__name__)

    # initialize configs
    app.config.from_object(Config)
    app.config.from_pyfile('credentials.py')

    init_logs(app)

    # initialize a bot instance
    app.bot = Bot(app.config['BOT_NAME'],
                      app.config['DATABASE_FILE'],
                      app.config['DEFAULT_RESPONSE'])

    # initialize a telegram instance
    from app.main import bp as main_bp
    with app.app_context():
        app.telegram = TelegramBotManager(app.config['TELEGRAM_API_KEY'])
        app.telegram.init()
        app.register_blueprint(main_bp)

    return app


def init_logs(app):
    """
    Setting logs up
    :param app:
    :return:
    """
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/myunibot_database.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)

