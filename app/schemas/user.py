
from pydantic import BaseModel, EmailStr, ConfigDict, StringConstraints, field_validator
from typing import Annotated, Any

class UserCreate(BaseModel):

    name: Annotated[str,StringConstraints(strip_whitespace=True, min_length=1)]
    email: EmailStr
    password: Annotated[str,StringConstraints(min_length=8, max_length=12)]

    

