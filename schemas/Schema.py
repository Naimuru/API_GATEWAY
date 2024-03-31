import strawberry
from .CommentsSchema import QueryComment,QueryUser
from .RatingSchema import QueryRating,MutationsRating
from .CommentsSchema import MutationsComment

@strawberry.type
class Query(QueryComment,QueryRating):
    pass

@strawberry.type
class Mutation(MutationsComment,MutationsRating):
    pass