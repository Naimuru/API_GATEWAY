import typing
import strawberry
import datetime
from utilities import *
from server import COMMENTS_URL_BASE
from ms_types.CommentsTypes import *


@strawberry.type
class QueryComment:
        
    @strawberry.field
    def comment(self,id:str)-> Comment:
        return generalRequest(COMMENTS_URL_BASE+"comments/{0}".format(id),GET)
    @strawberry.field
    def replies(self,parentId:str)->typing.List[Comment]:
        return generalRequest(COMMENTS_URL_BASE+"comments/{0}/replies".format(parentId),GET)
    
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest(COMMENTS_URL_BASE+"comments/",GET)
    @strawberry.field
    def itemComments(self,itemMusicId:str)->typing.List[Comment]:
        return generalRequest(COMMENTS_URL_BASE+"item/{0}/comments".format(itemMusicId),GET)
    @strawberry.field
    def userComments(self,userId:str)->typing.List[Comment]:
        return generalRequest(COMMENTS_URL_BASE+"user/{0}/comments".format(userId),GET)
    
    
    
    
@strawberry.type
class MutationsComment:

    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(COMMENTS_URL_BASE+"comments/{0}".format(id),PATCH,body=strawberry.asdict(comment))
    
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->Comment:
        return generalRequest(COMMENTS_URL_BASE+"comments/",POST,body=strawberry.asdict(comment))
    @strawberry.mutation
    def replyComment(self,parentId:str,reply:ReplyInput) -> Comment:
        parentComment=generalRequest(COMMENTS_URL_BASE+"comments/{0}".format(parentId),GET)
        print(parentComment)
        if(parentComment): #Validate if the comment to be replied actually exists
            reply.itemMusicId=parentComment["itemMusicId"]
            reply.parentId=parentId
            return generalRequest(COMMENTS_URL_BASE+"comments/{0}".format(parentId),POST,body=strawberry.asdict(reply))
        else:
            raise Exception("Comment to be replied doesn't exits")
    @strawberry.mutation
    def deleteComment(self,id:str) -> DeleteCommentResponse:
        response=generalRequest(COMMENTS_URL_BASE+"comments/{0}".format(id),DELETE)
        return response
    