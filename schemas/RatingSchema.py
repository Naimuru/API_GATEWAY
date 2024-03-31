import typing
import strawberry
import datetime
from utilities import *
from server import API_URL
from ms_types.RatingTypes import *


@strawberry.type
class QueryRating:
        
    @strawberry.field
    def rating(self,idUser:str,idItem:str)-> typing.List[Rating]:
        return generalRequest(API_URL+"calification/itemUser/{0}/{1}".format(idUser,idItem),GET)
    @strawberry.field
    def ratings(self)->typing.List[Rating]:
        return generalRequest(API_URL+"calification/all",GET)
    @strawberry.field
    def average(self,idItem:str)-> str:
        return generalRequest(API_URL+"calification/average/{0}".format(idItem),GET)

@strawberry.type
class MutationsRating:

    @strawberry.mutation
    def createRating(self,rating:RatingInput) ->Rating:
        response = generalRequest(API_URL+"calification/add",POST,body=strawberry.asdict(rating))
        return response

    @strawberry.mutation
    def updateRating(self,idUser:str,idItem:str,rating:RatingUpdate) -> str:
        return generalRequest(API_URL+"calification/{0}/{1}".format(idUser,idItem),PATCH,body=strawberry.asdict(rating))

    @strawberry.mutation
    def deleteRating(self,idUser:str,idItem:str) -> str:
        response=generalRequest(API_URL+"calification/{0}/{1}".format(idUser,idItem),DELETE)
        return response    
