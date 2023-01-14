from lib.postgresql import get_connection
from tables import user as user_table
from lib.security.password import verify_password
from .schemas.response import UserResponseSchema
from uuid import UUID

class AuthUser(UserResponseSchema):
    password: str

async def authenticate_user(email: str, password: str) -> AuthUser | None:
    query = user_table.select().where(user_table.c.email == email)
    user = await get_connection().fetch_one(query=query)
    if user:
        user = AuthUser.from_orm(user)
        if verify_password(password, user.password) == True:
            return user