import typing
import strawberry
from schemas.CommentsSchema import Comment,get_comments

@strawberry.type
class QueryAllComments:
    comments: typing.List[Comment] = strawberry.field(resolver=get_comments)