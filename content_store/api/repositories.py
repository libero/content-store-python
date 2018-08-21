from sqlalchemy.orm.exc import NoResultFound
from content_store.api.models import ArticlePart


class ArticlePartRepository:

    def __init__(self, db):

        self.db = db

    def add_article_part(self, article_part: ArticlePart) -> None:

        self.db.session.add(article_part)

    def delete_article_part(self, article_id, version, part_name) -> None:

        try:
            article_part = self.db.session.query(ArticlePart).filter_by(
                article_id=article_id,
                version=version,
                part_name=part_name
            ).one()
            self.db.session.delete(article_part)
        except NoResultFound:
            pass

    def get_article_part(self, article_id, version, part_name) -> ArticlePart:

        article_part = self.db.session.query(ArticlePart).filter_by(
            article_id=article_id,
            version=version,
            part_name=part_name
        ).one()
        return article_part
