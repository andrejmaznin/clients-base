from lib.security.passwords import verify_password

from modules.user.schemas.source import UserSourceSchema


async def authenticate_user(email: str, password: str) -> UserSourceSchema | None:
    u = await UserSourceSchema.get_by_email(email)
    if u is not None and verify_password(password, u.password):
        return u
