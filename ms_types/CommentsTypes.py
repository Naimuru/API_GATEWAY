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
    createdAt: str
    updatedAt: str

@strawberry.input
class CommentUpdate:
    content: str

@strawberry.input
class CommentInput:
    userId: str
    content: str
    itemMusicId: str

@strawberry.input
class ReplyInput:
    content: str
    userId: str
    itemMusicId: typing.Optional[str]=None
    parentId: typing.Optional[str]=None
@strawberry.type
class DeleteCommentResponse:
    acknowledged: str
    deletedCount: int