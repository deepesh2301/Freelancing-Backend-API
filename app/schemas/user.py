from pydantic import BaseModel, EmailStr,Field

class UserCreate(BaseModel):

    full_name: str = Field(..., min_length=3, max_length=100)  
    email:EmailStr
    password: str = Field(..., min_length=8)
    phone:str = Field(..., min_length=10, max_length=15)
    role_id:int

class UserLogin(BaseModel):
    email:EmailStr
    password:str
