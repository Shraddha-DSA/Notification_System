from pydantic import BaseModel, Field, EmailStr
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str
class UserLogin(BaseModel):
    email: EmailStr
    password:str