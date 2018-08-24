import pytest
from flask import Flask
from flask.testing import FlaskClient
from content_store.api.api import create_app
from content_store.api.config import TestingConfig
from content_store.api.database import DB


@pytest.fixture(name="app")
def application() -> Flask:
    """
    Flask application fixture
    :return: flask application fixture
    """
    app = create_app(config=TestingConfig)
    with app.app_context():
        DB.drop_all()
        DB.create_all()
        yield app


@pytest.fixture()
def client(app) -> FlaskClient:
    return app.test_client()
