from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserDTO(BaseModel):
    id: Optional[int]
    name: str
    email: EmailStr
    password: str
    created_at: Optional[datetime]

