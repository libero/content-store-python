from content_store.api.database import DB

ID_LENGTH = 100
PART_NAME_LENGTH = 100


class ArticlePart(DB.Model):
    article_id = DB.Column(DB.String(ID_LENGTH), primary_key=True)
    version = DB.Column(DB.Integer(), primary_key=True)
    part_name = DB.Column(DB.String(PART_NAME_LENGTH), primary_key=True)
    content = DB.Column(DB.Text())

    def __init__(self, article__id: str, version: int, part_name: str, content=str) -> None:
        self.article_id = article__id
        self.version = version
        self.part_name = part_name
        self.content = content

    def __repr__(self) -> str:
        return "<ArticlePart {id}->{version}->{part_name}>".format(
            id=self.article_id,
            version=self.version,
            part_name=self.part_name
        )
