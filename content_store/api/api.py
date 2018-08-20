import os
import json
from uuid import uuid4

from flask import Flask, make_response, request

from content_store.api.models import PlaceholderArticleVersion
from content_store.api.database import db
from content_store.api.config import DevelopmentConfig


def create_app(config=None):
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
    db.init_app(app)

    # TODO : add migrations
    with app.app_context():
        db.create_all()

    # could move to blueprint
    @app.route("/ping")
    def ping():
        """
        simple pingpong responder
        :return: response with content "pong"
        """
        resp = make_response("pong")
        resp.headers["Cache-Control"] = "no-store, must-revalidate"
        resp.headers["Content-Type"] = "text/plain; charset=utf-8"
        if request.environ.get("SERVER_PROTOCOL") == "HTTP/1.0":
            resp.headers["Expires"] = 0
        return resp

    @app.route("/testdb", methods=["POST"])
    def testdb():
        """
        temporary route to test persistence
        :return:
        """
        article_version = PlaceholderArticleVersion(str(uuid4()), 1, "Article content test")
        db.session.add(article_version)
        db.session.commit()
        response = make_response(json.dumps("done"))
        response.headers["Content-Type"] = "application/json"
        return response

    return app
