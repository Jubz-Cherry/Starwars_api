from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class LoginSchema(BaseModel):
    email: str
    password: str
    
    model_config = ConfigDict(from_attributes=True)
        
class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)
  
class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
    