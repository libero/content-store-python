from pathlib import Path
from lxml import etree

CONTENT_ID_EG = "el001"
VERSION_EG = 1
PART_NAME_EG = "front"


def test_content_put_get(client):
    """
    test content put and part get endpoints
    :param client: Flask test client
    """
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/content_1.xml")
    content = path.read_bytes()
    original_tree = etree.fromstring(content)
    original_front_element = original_tree.find("{http://libero.pub}front")
    original_front_text = etree.tostring(original_front_element).strip()

    put_content_response = client.put(
        f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_content_response.status_code == 201
    get_part_response = client.get(f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert get_part_response
    response_tree = etree.fromstring(get_part_response.data.decode())
    response_text = etree.tostring(response_tree)

    assert response_text == original_front_text


def test_content_not_found(client):
    """
    test unknown content
    :param client: Flask test client
    """
    prefix = client.application.config['PREFIX']

    response = client.get(f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert response.status_code == 404


def test_invalid_part(client):
    """
    test content put of invalid part
    :param client: Flask test client
    """
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/invalid_part.xml")
    content = path.read_bytes()

    put_content_response = client.put(
        f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_content_response.status_code == 400


def test_content_update(client):
    """
    test content put and part get endpoints
    :param client: Flask test client
    """
    prefix = client.application.config['PREFIX']

    path = Path("tests/fixtures/content_1.xml")
    content = path.read_bytes()

    put_content_response = client.put(
        f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_content_response.status_code == 201

    path = Path("tests/fixtures/content_2.xml")
    content = path.read_bytes()
    original_tree = etree.fromstring(content)
    original_front_element = original_tree.find("{http://libero.pub}front")
    update_front_text = etree.tostring(original_front_element).strip()

    put_content_response = client.put(
        f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}",
        data=content
    )
    assert put_content_response.status_code == 200

    get_part_response = client.get(f"/{prefix}/{CONTENT_ID_EG}/versions/{VERSION_EG}/{PART_NAME_EG}")
    assert get_part_response
    response_tree = etree.fromstring(get_part_response.data.decode())
    response_text = etree.tostring(response_tree)

    assert response_text == update_front_text
