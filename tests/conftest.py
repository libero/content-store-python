import pytest
from flask.testing import FlaskClient
from content_store.api.api import create_app
from content_store.api.config import TestingConfig
from content_store.api.database import DB


@pytest.fixture(name="app")
def application() -> FlaskClient:
    """
    Flask application fixture
    :return: flask application fixture
    """
    app = create_app(config=TestingConfig)
    with app.app_context():
        DB.drop_all()
        DB.create_all()
        yield app
