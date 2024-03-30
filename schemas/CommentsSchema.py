import typing
import strawberry
from utilities import *
@strawberry.type
class Comment:
    _id: str
    userId: str
    content: str
    parentId: typing.Optional[str]
    itemMusicId:str
    #Handle likes and dislikes
@strawberry.input
class CommentInput:
    userId: str
    content: str

@strawberry.type
class Query:
    @strawberry.field
    def comment(id:str)-> Comment:
        return generalRequest("http://localhost:8080/api/v1/comments/{0}".format(id),"GET")
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest("http://localhost:8080/api/v1/comments","GET")
    
    
def get_comments():
    return [
        generalRequest("http://localhost:8080/api/v1/comments","GET")
    ]
