from pathlib import Path
from lxml import etree

ARTICLE_ID_EG = "el001"
VERSION_EG = 1
PART_NAME_EG = "front"


def test_article_put_get(app):
    """
    test article put and part get endpoints
    :param app: Flask application
    """
    client = app.test_client()
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/content_1.xml")
    content = path.read_bytes()
    original_tree = etree.fromstring(content)
    original_front_element = original_tree.find("{http://libero.pub}front")
    original_front_text = etree.tostring(original_front_element).strip()

    put_article_response = client.put(
        f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_article_response.status_code == 201
    get_part_response = client.get(f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert get_part_response
    response_tree = etree.fromstring(get_part_response.data.decode())
    response_text = etree.tostring(response_tree)

    assert response_text == original_front_text


def test_article_not_found(app):
    """
    test unknown article
    :param app: Flask application
    """
    client = app.test_client()
    prefix = client.application.config['PREFIX']

    response = client.get(f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert response.status_code == 404


def test_invalid_part(app):
    """
    test article put of invalid part
    :param app: Flask application
    """
    client = app.test_client()
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/invalid_part.xml")
    content = path.read_bytes()

    put_article_response = client.put(
        f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_article_response.status_code == 400


def test_article_update(app):
    """
    test article put and part get endpoints
    :param app: Flask application
    """
    client = app.test_client()
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/content_1.xml")
    content = path.read_bytes()

    put_article_response = client.put(
        f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_article_response.status_code == 201

    path = Path("tests/fixtures/content_2.xml")
    content = path.read_bytes()
    original_tree = etree.fromstring(content)
    original_front_element = original_tree.find("{http://libero.pub}front")
    update_front_text = etree.tostring(original_front_element).strip()

    put_article_response = client.put(
        f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_article_response.status_code == 200

    get_part_response = client.get(f"/{prefix}/{ARTICLE_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert get_part_response
    response_tree = etree.fromstring(get_part_response.data.decode())
    response_text = etree.tostring(response_tree)

    assert response_text == update_front_text
