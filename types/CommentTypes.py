import strawberry
import typing
@strawberry.type
class Comment:
    _id: str
    userId: str
    content: str
    parentId: typing.Optional[str]
    itemMusicId:str
    likes: typing.List[str]
    dislikes: typing.List[str]


@strawberry.input
class CommentUpdate:
    content: str

@strawberry.input
class CommentInput:
    userId: str
    content: str
    itemMusicId: str
