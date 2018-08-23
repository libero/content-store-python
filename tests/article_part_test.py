import pytest
from sqlalchemy.orm.exc import NoResultFound
from content_store.api.models import ArticlePart
from content_store.api.repositories import ArticlePartRepository
from content_store.api.database import DB


@pytest.mark.usefixtures("client")
def test_add_get_parts():
    """
    test adding and retrieving a part
    """
    article_parts = ArticlePartRepository(DB)

    test_parts = (
        ArticlePart("001", 1, "front", "Article 001 front matter content v1"),
        ArticlePart("001", 1, "body", "Article 001 body content v1"),
        ArticlePart("002", 1, "front", "Article 002 front matter content v1"),
        ArticlePart("002", 1, "body", "Article 002 front matter content v1")
    )
    for part in test_parts:
        article_parts.add_or_update_article_part(part)

        assert part == article_parts.get_article_part(
            article_id=part.article_id,
            version=part.version,
            part_name=part.part_name
        )

        assert str(part) == f"<ArticlePart {part.article_id}->{part.version}->{part.part_name}>"


@pytest.mark.usefixtures("client")
def test_delete_part():
    """
    test deletion of a part
    """
    article_parts = ArticlePartRepository(DB)
    test_part = ArticlePart("001", 1, "front", "Article 001 front matter content v1")
    article_parts.add_or_update_article_part(test_part)
    part = article_parts.get_article_part(
        test_part.article_id,
        test_part.version,
        test_part.part_name
    )

    assert part == test_part

    article_parts.delete_article_part(
        part.article_id,
        part.version,
        part.part_name
    )

    with pytest.raises(NoResultFound):
        article_parts.get_article_part(
            test_part.article_id,
            test_part.version,
            test_part.part_name
        )


@pytest.mark.usefixtures("client")
def test_delete_unknown_part():
    """
    test deletion of a part
    """
    article_parts = ArticlePartRepository(DB)
    test_part = ArticlePart("998", 1, "front", "Article 001 front matter content v1")

    article_parts.delete_article_part(
        test_part.article_id,
        test_part.version,
        test_part.part_name
    )
    # should succeed without error
