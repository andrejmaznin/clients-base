from jose import JWTError, jwt
from os import getenv
from modules.user.schemas.source import UserSourceSchema, user
from .exceptions import DecodeException

ALGORITHM = 'HS256'
SECRET_KEY = getenv('SECRET_KEY')


def create_access_token(data: dict) -> str | None:
    data['id'] = str(data['id'])
    del data['birthdate']
    if SECRET_KEY:
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    return None


async def get_current_user(token: str) -> UserSourceSchema | None:
    if SECRET_KEY:
        try:
            uuid = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('id')
            
            if uuid:
                return await UserSourceSchema.myget(user.c.id==uuid)

        except JWTError as e:
            raise DecodeException()
    return None

