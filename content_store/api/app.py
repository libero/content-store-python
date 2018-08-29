import os
from flask import Flask

from content_store.api import api
from content_store.api.database import DB
from content_store.api.config import DevelopmentConfig
from content_store.api.repositories import ContentPartRepository


def create_app(config=None) -> Flask:
    """
    application factory
    :param config: override config
    :return: application
    """
    app = Flask(__name__)

    # basic configurations setup for now
    if config:
        app.config.from_object(config)
    else:
        if "APP_SETTINGS" in os.environ:
            app.config.from_object(os.environ["APP_SETTINGS"])
        else:
            app.config.from_object(DevelopmentConfig)
    DB.init_app(app)

    # create tables if required, will be replaced by migrations
    with app.app_context():
        DB.create_all()

    part_repo = ContentPartRepository(DB)

    app.register_blueprint(api.create_blueprint(part_repo), url_prefix='/' + app.config["PREFIX"])

    return app
