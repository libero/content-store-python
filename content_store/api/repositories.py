from sqlalchemy.orm.exc import NoResultFound
from content_store.api.models import ContentPart


class ContentPartRepository:

    def __init__(self, database) -> None:

        self.database = database

    def add_or_update_content_part(self, content_part: ContentPart) -> bool:
        """
        :param content_part: part to add
        :return: True for add or false for update
        """
        added_not_updated = False
        if self.part_exists(content_part.content_id, content_part.version, content_part.part_name):
            self.database.session.merge(content_part)
        else:
            self.database.session.add(content_part)
            added_not_updated = True
        self.database.session.commit()
        return added_not_updated

    def delete_content_part(self, content_id, version, part_name) -> None:

        try:
            content_part = self.database.session.query(ContentPart).filter_by(
                content_id=content_id,
                version=version,
                part_name=part_name
            ).one()
            self.database.session.delete(content_part)
            self.database.session.commit()
        except NoResultFound:
            pass

    def get_content_part(self, content_id, version, part_name) -> ContentPart:

        content_part = self.database.session.query(ContentPart).filter_by(
            content_id=content_id,
            version=version,
            part_name=part_name
        ).one()
        return content_part

    def part_exists(self, content_id, version, part_name):

        try:
            self.database.session.query(ContentPart).filter_by(
                content_id=content_id,
                version=version,
                part_name=part_name
            ).one()
        except NoResultFound:
            return False

        return True
