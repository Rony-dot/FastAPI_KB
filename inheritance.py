class Pydantic:
    def is_valid(self,text):
        if "admin" in text:
            return False
        return True

class Starlette:
    def is_valid(self,text):
        return True

class FastAPI(Pydantic, Starlette):
    pass

f = FastAPI()
print(f.is_valid("admin is trying to sign in")) # False, because in python, multiple inheritance prefers the first class that is inherits
print(FastAPI.__mro__) # prints the hiararchy of inherited classes