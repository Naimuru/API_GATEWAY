import typing
import strawberry
import datetime
from utilities import *
from server import API_URL
#from types.CommentTypes import Comment




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
@strawberry.type
class Query:
        
    @strawberry.field
    def comment(self,id:str)-> Comment:
        return generalRequest(API_URL+"comments/{0}".format(id),GET)
    @strawberry.field
    def replies(self,parentId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"comments/{0}/replies".format(parentId),GET)
    
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest(API_URL+"comments/",GET)
    @strawberry.field
    def itemComments(self,itemMusicId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"item/{0}/comments".format(itemMusicId),GET)
    @strawberry.field
    def userComments(self,userId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"user/{0}/comments".format(userId),GET)
    
    
    
    
@strawberry.type
class Mutations:

    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(API_URL+"comments/{0}".format(id),PATCH,body=strawberry.asdict(comment))
    
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->Comment:
        return generalRequest(API_URL+"comments/",POST,body=strawberry.asdict(comment))
    @strawberry.mutation
    def replyComment(self,parentId:str,reply:ReplyInput) -> Comment:
        parentComment=generalRequest(API_URL+"comments/{0}".format(parentId),GET)
        print(parentComment)
        if(parentComment): #Validate if the comment to be replied actually exists
            reply.itemMusicId=parentComment["itemMusicId"]
            reply.parentId=parentId
            return generalRequest(API_URL+"comments/{0}".format(parentId),POST,body=strawberry.asdict(reply))
        else:
            raise Exception("Comment to be replied doesn't exits")
    @strawberry.mutation
    def deleteComment(self,id:str) -> DeleteCommentResponse:
        response=generalRequest(API_URL+"comments/{0}".format(id),DELETE)
        return response