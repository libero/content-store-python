from content_store.api.database import db

ID_LENGTH = 36


class ArticleVersion(db.Model):

    id = db.Column(db.String(ID_LENGTH), primary_key=True)
    version = db.Column(db.Integer())
    content = db.Column(db.Text())

    def __init__(self, id: str, version: int, content=str) -> None:

        self.id = id
        self.version = version
        self.content = content

    def __repr__(self) -> str:
        return "<ArticleVersion {id} {version}>".format(id=self.id, version=self.version)
