import pytest
from content_store.api.api import create_app
from content_store.api.config import TestingConfig


@pytest.fixture(name="client")
def _client():

    app = create_app(config=TestingConfig)
    ctx = app.app_context()
    ctx.push()

    yield app.test_client()

    ctx.pop()


def test_api_ping(client):
    """
    test pingpong endpoint
    :param client: client fixture
    """

    res = client.get("/ping")
    assert res.data == b"pong"
    assert res.headers["Cache-Control"] == "no-store, must-revalidate"
    assert res.headers["Content-Type"] == "text/plain; charset=utf-8"
