def test_api_ping(client):
    """
    test pingpong endpoint
    :param client: flask application test client
    """
    res = client.get("/ping")
    assert res.data == b"pong"
    assert res.headers["Cache-Control"] == "no-store, must-revalidate"
    assert res.headers["Content-Type"] == "text/plain; charset=utf-8"
