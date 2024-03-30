from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from strawberry.schema.config import StrawberryConfig
from schemas.CommentsSchema import Query
import operator
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



def default_resolver(root, field):
    try:
        return operator.getitem(root, field)
    except KeyError:
        return getattr(root, field)

config = StrawberryConfig(
    default_resolver=default_resolver
)

schema= strawberry.Schema(query=Query,config=config)


app=FastAPI()
@app.get("/")
def index(): 
    return {"mess":"a"}
app.add_route("/graphql",GraphQL(schema,debug=True))
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)