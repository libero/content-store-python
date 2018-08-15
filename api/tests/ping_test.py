import pytest
from flask import url_for
from api.api import create_app


@pytest.fixture
def client():

    app = create_app(debug=True)
    ctx = app.app_context()
    ctx.push()

    # eventual db init
    client = app.test_client()

    yield client

    # eventual db cleanup
    ctx.pop()


def test_api_ping(client):

    res = client.get('/ping')
    assert res.data == b"pong"
