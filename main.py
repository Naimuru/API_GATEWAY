from fastapi import FastAPI
import strawberry
from resolvers import QueryComment
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

schema= strawberry.Schema(query=QueryComment)