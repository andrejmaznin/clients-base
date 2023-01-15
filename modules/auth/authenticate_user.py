from lib.security.password import verify_password
from modules.user.schemas.source import UserSourceSchema, user

async def authenticate_user(email: str, password: str) -> UserSourceSchema | None:
    u = await UserSourceSchema.myget(user.c.email == email)
    if u != None and verify_password(password, u.password) == True:
        return u