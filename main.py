from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

myapp = FastAPI()

@myapp.get('/blog')
def index(limit, published:bool = True, sort:Optional[str] = None):
    if published:
        return {'data':f'{limit} blog list from the db'}
    else:
        return {'data':f'{limit} blog list from the db'}

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@myapp.get('/blog/{id}')
def show(id:int):
    return {'data':id}



@myapp.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of that id = id
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@myapp.post('/blog')
def create_blog(request:Blog):
    return {'data':f"Blog is created with {request.title}"}

#if __name__ =="__main__":
#    uvicorn.run(myapp,host="127.0.0.1",port= '9000')

