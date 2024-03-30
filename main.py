from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from resolvers.Comments import QueryComment
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

schema= strawberry.Schema(query=QueryComment)


app=FastAPI()
@app.get("/")
def index(): 
    return {"mess":"a"}
app.add_route("/graphql",GraphQL(schema,debug=True))
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)