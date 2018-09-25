from flask import Blueprint, make_response, request
from lxml import etree
from sqlalchemy.orm.exc import NoResultFound

from content_store.api.models import ContentPart
from content_store.api.repositories import ContentPartRepository


def create_blueprint(part_repo: ContentPartRepository) -> Blueprint:
    blueprint = Blueprint('api', __name__)

    @blueprint.route("/ping")
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

    @blueprint.route("/<string:content_id>/versions/<int:version>", methods=["PUT"])
    def _put_version(content_id, version):
        """
        :param content_id: id of the content
        :param version: version of the content
        :return: status string
        """
        root = etree.fromstring(request.get_data())
        # Could validate against schema here

        front = root.find("{http://libero.pub}front")
        if front is None:
            return "invalid content", 400

        front_text = etree.tostring(front).strip()

        part = ContentPart(content_id, version, 'front', front_text)
        added_not_updated = part_repo.add_or_update_content_part(part)
        status = 201 if added_not_updated else 200
        resp = make_response("done", status)

        return resp

    @blueprint.route("/<string:content_id>/versions/<int:version>/<string:part_name>",
                     methods=["GET"])
    def _get_part(content_id, version, part_name):
        """
        :param content_id: id of the content
        :param version: version of the content
        :param part_name: the name of the part
        :return: the xml content of the specified part or a status string if unsucessful
        """
        # could validate part name here
        try:
            part = part_repo.get_content_part(content_id, version, part_name)
        except NoResultFound:
            return "part not found", 404

        resp = make_response(part.content)
        resp.headers["Content-Type"] = "text/xml; charset=utf-8"
        return resp

    return blueprint
