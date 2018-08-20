from content_store.api.database import DB

ID_LENGTH = 100


class PlaceholderArticleVersion(DB.Model):

    id = DB.Column(DB.String(ID_LENGTH), primary_key=True)
    version = DB.Column(DB.Integer())
    content = DB.Column(DB.Text())

    def __init__(self, av_id: str, version: int, content=str) -> None:

        self.id = av_id
        self.version = version
        self.content = content

    def __repr__(self) -> str:
        return "<ArticleVersion {id} {version}>".format(id=self.av_id, version=self.version)
