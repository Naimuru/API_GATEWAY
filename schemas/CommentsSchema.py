import typing
import strawberry
@strawberry.type
class Comment:
    _id: str
    userId: str
    content: str
    parentId: str
    itemMusicId:str
    #Handle likes and dislikes
def get_comments():
    return [
        Comment(
            _id= "28393314k",
            userId= "3272432jkelads",
            content= "This is a comment example",
            parentId= "parent18290483209",
            itemMusicId="cerati239028942",
        ),
    ]
