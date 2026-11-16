
from pydantic import BaseModel, EmailStr, ConfigDict, StringConstraints, field_validator
from typing import Annotated, Any
from datetime import datetime

class UserCreate(BaseModel):

    name: Annotated[str,StringConstraints(strip_whitespace=True, min_length=1)]
    email: EmailStr
    password: Annotated[str,StringConstraints(min_length=8, max_length=12)]

    @field_validator("email", mode="before")
    @classmethod
    def normalize_email(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip().lower()
        return value
    
class UserRead(BaseModel):

    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)