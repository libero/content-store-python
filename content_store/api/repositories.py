from content_store.api.database import db
from content_store.api.models import ArticleVersion


def add_article_version():

    av = ArticleVersion("abc", 1, "random content")
    db.session.add(av)
    db.session.commit()
