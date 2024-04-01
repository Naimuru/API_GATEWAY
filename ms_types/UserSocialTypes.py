import strawberry
import typing
@strawberry.type
class User:
    uid: str
    emailAddr: str
    userName: str
    nickname: str
    keyIdAuth: str
    description: str
    arrArtists: typing.Optional[typing.List[str]]
    arrTracks: typing.Optional[typing.List[str]]
    arrAlbums: typing.Optional[typing.List[str]]
@strawberry.type
class UserDeleteResponse:
    success: str  
@strawberry.type
class FollowResponse:
    result: typing.Optional[bool]
# Input Types  
@strawberry.input
class UserInput:
    emailAddr: str
    userName: str
    nickname: str
    keyIdAuth: str
    description: str
@strawberry.input
class UserDeleteInput:
    userName: str
@strawberry.input
class UserUpdateInput:
    nickname: str
    description: str
    arrArtists: typing.Optional[typing.List[str]]=None
    arrTracks: typing.Optional[typing.List[str]]=None
    arrAlbums: typing.Optional[typing.List[str]]=None
@strawberry.input
class FollowInput:
    uid1: str
    uid2: str

    