import pytest
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
    """
    test pingpong endpoint
    :param client: client fixture
    """
    res = client.get('/ping')
    assert res.data == b"pong"
    assert res.headers['Cache-Control'] == "no-store, must-revalidate"
    assert res.headers['Content-Type'] == "text/plain; charset=utf-8"
