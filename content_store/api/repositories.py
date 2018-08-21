from sqlalchemy.orm.exc import NoResultFound
from content_store.api.database import DB
from content_store.api.models import ArticlePart


class ArticlePartRepository:

    def add_article_part(self, av: ArticlePart) -> None:

        DB.session.add(av)
        DB.session.commit()

    def delete_article_part(self, id, version, part_name) -> None:

        try:
            article_part = DB.session.query(ArticlePart).filter_by(id=id, version=version,
                                                                   part_name=part_name).one()
            DB.session.delete(article_part)
        except NoResultFound:
            pass

    def get_article_part(self, id, version, part_name) -> ArticlePart:

        article_part = DB.session.query(ArticlePart).filter_by(id=id, version=version,
                                                               part_name=part_name).one()
        return article_part
