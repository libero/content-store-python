import pytest
from sqlalchemy.orm.exc import NoResultFound
from content_store.api.api import create_app
from content_store.api.config import TestingConfig
from content_store.api.models import ArticlePart
from content_store.api.repositories import ArticlePartRepository
from content_store.api.database import DB


@pytest.fixture
def app():

    application = create_app(TestingConfig)
    with application.app_context():
        DB.drop_all()
        DB.create_all()
        yield application


def test_add_get_parts(app):

    article_parts = ArticlePartRepository()

    test_parts = (
        ArticlePart("001", 1, "front", "Article 001 front matter content v1"),
        ArticlePart("001", 1, "body", "Article 001 body content v1"),
        ArticlePart("002", 1, "front", "Article 002 front matter content v1"),
        ArticlePart("002", 1, "body", "Article 002 front matter content v1")
    )
    for part in test_parts:
        article_parts.add_article_part(part)

        assert part == article_parts.get_article_part(id=part.id, version=part.version, part_name=part.part_name)


def test_delete_part(app):

    with app.app_context():

        article_parts = ArticlePartRepository()
        test_part = ArticlePart("001", 1, "front", "Article 001 front matter content v1")
        article_parts.add_article_part(test_part)
        part = article_parts.get_article_part(test_part.id, test_part.version, test_part.part_name)
        assert part == test_part
        article_parts.delete_article_part(part.id, part.version, part.part_name)
        with pytest.raises(NoResultFound):
            part_again = article_parts.get_article_part(test_part.id, test_part.version, test_part.part_name)

