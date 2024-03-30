import typing
import strawberry
from utilities import *
@strawberry.type
class Comment:
    _id: str
    userId: str
    content: str
    parentId: str
    itemMusicId:str
    #Handle likes and dislikes
@strawberry.input
class CommentInput:
    userId: str
    content: str
def get_comments():
    return [
        generalRequest("http://localhost:8080/api/v1/comments","GET")
    ]
