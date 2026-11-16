
from app.schemas.user import UserRead
from app.models.user import User
from datetime import datetime


def test_user_head():
    user = User(
        id = 1,
        name = "frank",
        email = "frank@gmail.com",
        password_hash = "ww4yw4y5",
        created_at = datetime(2026,11,15,19,30),
        updated_at = datetime(2026,11,15,19,30)
    )
    
    result = UserRead.model_validate(user)

    assert result.id == 1
    assert result.name == "frank"
    assert result.email == "frank@gmail.com"
    assert "password_hash" not in result.model_dump()
    assert isinstance(result.created_at, datetime)
    assert isinstance(result.updated_at, datetime)
