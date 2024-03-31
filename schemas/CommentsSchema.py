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

@strawberry.type
class Query:
        
    @strawberry.field
    def comment(self,id:str)-> Comment:
        #return generalRequest(url_comments+id,"GET")
        return generalRequest(API_URL+"comments/{0}".format(id),"GET")
    @strawberry.field
    def replies(self,parentId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"comments/{0}/replies".format(parentId),"GET")
    
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest(API_URL+"comments/","GET")
    @strawberry.field
    def itemComments(self,itemMusicId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"item/{0}/comments".format(itemMusicId),"GET")
    @strawberry.field
    def userComments(self,userId:str)->typing.List[Comment]:
        return generalRequest(API_URL+"user/{0}/comments".format(userId),"GET")
    
    
    
    
@strawberry.type
class Mutations:

    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(API_URL+"comments/{0}".format(id),"PATCH",body=strawberry.asdict(comment))
    
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->Comment:
        return generalRequest(API_URL+"comments/","POST",body=strawberry.asdict(comment))

        

# def jsonToComment(jsonbObject)->Comment:
#     print(type(jsonbObject))
#     dictionary=json.loads(jsonbObject.decode('utf-8'))
#     print("_____")
#     print(dictionary)
#     comment= Comment(
#         _id= dictionary["_id"],
#         userId= dictionary["userId"],
#         content= dictionary["content"],
#         itemMusicId=dictionary["itemMusicId"],
#         likes= dictionary["likes"],
#         dislikes= dictionary["dislikes"],
#         createdAt= dictionary["createdAt"],
#         updatedAt= dictionary["updatedAt"]
#     )
#     if "parentId" in dictionary:
#         comment.parentId=dictionary["parentId"]
#     return comment