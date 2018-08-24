import pytest
from sqlalchemy.orm.exc import NoResultFound
from content_store.api.models import ContentPart
from content_store.api.repositories import ContentPartRepository
from content_store.api.database import DB


@pytest.mark.usefixtures("app")
def test_add_get_parts():
    """
    test adding and retrieving a part
    """
    content_parts = ContentPartRepository(DB)

    test_parts = (
        ContentPart("001", 1, "front", "Content 001 front matter content v1"),
        ContentPart("001", 1, "body", "Content 001 body content v1"),
        ContentPart("002", 1, "front", "Content 002 front matter content v1"),
        ContentPart("002", 1, "body", "Content 002 front matter content v1")
    )
    for part in test_parts:
        content_parts.add_or_update_content_part(part)

        assert part == content_parts.get_content_part(
            content_id=part.content_id,
            version=part.version,
            part_name=part.part_name
        )

        assert str(part) == f"<ContentPart {part.content_id}->{part.version}->{part.part_name}>"


@pytest.mark.usefixtures("app")
def test_delete_part():
    """
    test deletion of a part
    """
    content_parts = ContentPartRepository(DB)
    test_part = ContentPart("001", 1, "front", "Content 001 front matter content v1")
    content_parts.add_or_update_content_part(test_part)
    part = content_parts.get_content_part(
        test_part.content_id,
        test_part.version,
        test_part.part_name
    )

    assert part == test_part

    content_parts.delete_content_part(
        part.content_id,
        part.version,
        part.part_name
    )

    with pytest.raises(NoResultFound):
        content_parts.get_content_part(
            test_part.content_id,
            test_part.version,
            test_part.part_name
        )


@pytest.mark.usefixtures("app")
def test_delete_unknown_part():
    """
    test deletion of an unknown part
    """
    content_parts = ContentPartRepository(DB)
    test_part = ContentPart("998", 1, "front", "Content 001 front matter content v1")

    content_parts.delete_content_part(
        test_part.content_id,
        test_part.version,
        test_part.part_name
    )
    # should succeed without error
