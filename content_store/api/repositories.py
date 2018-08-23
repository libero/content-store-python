from sqlalchemy.orm.exc import NoResultFound
from content_store.api.models import ArticlePart


class ArticlePartRepository:

    def __init__(self, database) -> None:

        self.database = database

    def add_or_update_article_part(self, article_part: ArticlePart) -> bool:
        """
        :param article_part: part to add
        :return: True for add or false for update
        """
        added_not_updated = False
        try:
            self.get_article_part(article_part.article_id, article_part.version, article_part.part_name)
            self.database.session.merge(article_part)
        except NoResultFound:
            self.database.session.add(article_part)
            added_not_updated = True
        self.database.session.commit()
        return added_not_updated

    def delete_article_part(self, article_id, version, part_name) -> None:

        try:
            article_part = self.database.session.query(ArticlePart).filter_by(
                article_id=article_id,
                version=version,
                part_name=part_name
            ).one()
            self.database.session.delete(article_part)
            self.database.session.commit()
        except NoResultFound:
            pass

    def get_article_part(self, article_id, version, part_name) -> ArticlePart:

        article_part = self.database.session.query(ArticlePart).filter_by(
            article_id=article_id,
            version=version,
            part_name=part_name
        ).one()
        return article_part
