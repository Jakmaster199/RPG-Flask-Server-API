from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import os

environment = os.getenv('FLASK_ENV')

myApp = Flask(__name__)
myLog = myApp.logger

gunicorn_logger = logging.getLogger('gunicorn.error')
myApp.logger.handlers = gunicorn_logger.handlers
myApp.logger.setLevel(gunicorn_logger.level)

try:
    myApp.config.from_object('app.settings.%s' % environment)
    myLog.info("Configuration loaded for '%s' environment." % environment)

except Exception as e:
    myLog.error("Please, define environment variable 'FLASK_ENV' with one of this values: 'Development', 'Production'.")
    myApp.config.from_object('app.settings.Development')

myDb = SQLAlchemy(myApp)

try:
    from app.blueprints import default, accounts
    myApp.register_blueprint(default.BP, url_prefix='/')
    myApp.register_blueprint(accounts.BP, url_prefix='/account')
except Exception as e:
    myLog.error('Unable to load Blueprints: (%s)' % e)
