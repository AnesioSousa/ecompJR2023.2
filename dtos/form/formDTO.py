from typing import Optional
from pydantic import BaseModel, EmailStr

class FormDTO(BaseModel):
    id: Optional[int]
    client_name: str
    client_email: EmailStr
    service_description: str

