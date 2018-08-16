from flask import Flask, Response, request


def create_app(debug=False):
    """
    application factory
    :param debug: set application to debug
    :return: application
    """

    app = Flask(__name__)
    app.debug = debug

    # could move to blueprint
    @app.route("/ping")
    def ping():
        """
        simple pingpong responder
        :return: response with content "pong"
        """
        resp = Response("pong")
        resp.headers["Cache-Control"] = "no-store, must-revalidate"
        resp.headers["Content-Type"] = "text/plain; charset=utf-8"
        if request.environ.get("SERVER_PROTOCOL") == "HTTP/1.0":
            resp.headers["Expires"] = 0
        return resp

    return app
