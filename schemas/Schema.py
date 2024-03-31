import strawberry
from .CommentsSchema import CommentQueries,CommentMutations
from .UserSocialSchema import UserSocialQueries,UserSocialMutations
@strawberry.type
class Query(CommentQueries,
            UserSocialQueries):
    pass
@strawberry.type
class Mutation(CommentMutations
               ,UserSocialMutations):
    pass