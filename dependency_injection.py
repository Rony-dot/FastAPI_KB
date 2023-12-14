from typing import Any
from fastapi import FastAPI, Depends, HTTPException, status
# example of dependency injection in python
blogs = {
    "1":"blog 1",
    "2":"blog 2",
    "3":"blog 3"
}

users = {
    "8":"user name 8",
    "9":"user name 9",
    "10":"user name 10",
}
app = FastAPI(title="dependency injection" ,version="1.1.1")


@app.get("/")
def home_page():
    return {"msg":"this is home page"};

class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model
    def __call__(self, id) -> Any:
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail="obj not exists with this id",status_code=status.HTTP_404_NOT_FOUND)
        return obj

blog_dependency = GetObjectOr404(blogs)
@app.get("/blogs/{id}")
def get_blog(blog_name:str = Depends(blog_dependency)):
    return blog_name

user_dependency = GetObjectOr404(users)
@app.get("/users/{id}")
def get_blog(user_name:str = Depends(user_dependency)):
    return user_name


# the junior approach
# def get_blog_or_404(id: str):
#     blog_name = blogs.get(id)
#     if not blog_name:
#         # return {"msg":"blog not exists with this id"}
#         raise HTTPException(detail="blog not exists with this id",status_code=status.HTTP_404_NOT_FOUND)
#     return blog_name


# @app.get("/blogs/{id}")
# def get_blog(blog_name:str = Depends(get_blog_or_404)):
#     return blog_name