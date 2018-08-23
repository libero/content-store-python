import os
from lxml import etree
from flask import Flask, make_response, request
from sqlalchemy.orm.exc import NoResultFound

from content_store.api.database import DB
from content_store.api.config import DevelopmentConfig
from content_store.api.models import ArticlePart
from content_store.api.repositories import ArticlePartRepository


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
    DB.init_app(app)

    # create tables if required, will be replaced by migrations
    with app.app_context():
        DB.create_all()

    # could move routes to blueprint

    @app.route("/ping")
    def _ping():
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

    @app.route("/" + app.config["PREFIX"] + "/<string:article_id>/versions/<int:version>", methods=["PUT"])
    def _put_version(article_id, version):

        root = etree.fromstring(request.get_data())
        # Could validate against schema here

        front = root.find("{http://libero.pub}front")
        if front is None:
            return "invalid content", 400

        front_text = etree.tostring(front).strip()
        part_repo = ArticlePartRepository(DB)

        part = ArticlePart(article_id, version, 'front', front_text)
        added_not_updated = part_repo.add_or_update_article_part(part)
        status = 201 if added_not_updated else 200
        resp = make_response("done", status)

        return resp

    @app.route("/" + app.config["PREFIX"] + "/<string:article_id>/versions/<int:version>/<string:part_name>",
               methods=["GET"])
    def _get_part(article_id, version, part_name):

        # could validate part name here
        part_repo = ArticlePartRepository(DB)
        try:
            part = part_repo.get_article_part(article_id, version, part_name)
        except NoResultFound:
            return "part not found", 404

        resp = make_response(part.content)
        resp.headers["Content-Type"] = "text/xml; charset=utf-8"
        return resp

    return app
