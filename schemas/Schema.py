import strawberry
from .CommentsSchema import QueryComment,QueryUser
@strawberry.type
class Query(QueryComment):
    pass