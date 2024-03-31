import typing
import strawberry
import datetime
from utilities import *
from server import RATING_URL_BASE
from ms_types.RatingTypes import *


@strawberry.type
class QueryRating:
        
    @strawberry.field
    def rating(self,idUser:str,idItem:str)-> typing.List[Rating]:
        return generalRequest(RATING_URL_BASE+"calification/itemUser/{0}/{1}".format(idUser,idItem),GET)
    @strawberry.field
    def ratings(self)->typing.List[Rating]:
        return generalRequest(RATING_URL_BASE+"calification/all",GET)
    @strawberry.field
    def average(self,idItem:str)-> str:
        return generalRequest(RATING_URL_BASE+"calification/average/{0}".format(idItem),GET)

@strawberry.type
class MutationsRating:

    @strawberry.mutation
    def createRating(self,rating:RatingInput) ->Rating:
        response = generalRequest(RATING_URL_BASE+"calification/add",POST,body=strawberry.asdict(rating))
        return response

    @strawberry.mutation
    def updateRating(self,idUser:str,idItem:str,rating:RatingUpdate) -> str:
        return generalRequest(RATING_URL_BASE+"calification/{0}/{1}".format(idUser,idItem),PATCH,body=strawberry.asdict(rating))

    @strawberry.mutation
    def deleteRating(self,idUser:str,idItem:str) -> str:
        response=generalRequest(RATING_URL_BASE+"calification/{0}/{1}".format(idUser,idItem),DELETE)
        return response    
