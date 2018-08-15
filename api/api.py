from flask import Flask


def create_app(debug=False):

    app = Flask(__name__)
    app.debug = debug

    # could move to blueprint
    @app.route("/ping")
    def ping():
        return "pong"

    return app
