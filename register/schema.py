from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class LoginSchema(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True
        
class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
  
class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    