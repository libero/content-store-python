from sqlalchemy.orm.exc import NoResultFound
from content_store.api.database import DB
from content_store.api.models import ArticlePart


class ArticlePartRepository:

    @staticmethod
    def add_article_part(article_part: ArticlePart) -> None:

        DB.session.add(article_part)

    @staticmethod
    def delete_article_part(article_id, version, part_name) -> None:

        try:
            article_part = DB.session.query(ArticlePart).filter_by(
                article_id=article_id,
                version=version,
                part_name=part_name
            ).one()
            DB.session.delete(article_part)
        except NoResultFound:
            pass

    @staticmethod
    def get_article_part(article_id, version, part_name) -> ArticlePart:

        article_part = DB.session.query(ArticlePart).filter_by(
            article_id=article_id,
            version=version,
            part_name=part_name
        ).one()
        return article_part
