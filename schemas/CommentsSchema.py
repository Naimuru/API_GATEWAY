import typing
import strawberry
import datetime
from utilities import *
from server import COMMENTS_API






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

@strawberry.type
class Query:
        
    @strawberry.field
    def comment(self,id:str)-> Comment:
        #return generalRequest(url_comments+id,"GET")
        return generalRequest(COMMENTS_API+"comments/{0}".format(id),"GET")
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest(COMMENTS_API+"comments/","GET")
    
    
@strawberry.type
class Mutations:
    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(COMMENTS_API+"comments/{0}".format(id),"PATCH",body=strawberry.asdict(comment))
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->Comment:
        return generalRequest(COMMENTS_API+"comments/{0}".format(id),"POST",body=strawberry.asdict  (comment))
    
        
    
