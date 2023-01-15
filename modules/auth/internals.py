
from lib.security.password import verify_password
from modules.user.schemas.source import UserSourceSchema

async def authenticate_user(email: str, password: str) -> UserSourceSchema | None:
    u = await UserSourceSchema.get_by_email(email)
    if u != None and verify_password(password, u.password) == True:
        return u