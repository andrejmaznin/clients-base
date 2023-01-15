from jose import JWTError, jwt
from os import getenv
from modules.user.schemas.source import UserSourceSchema
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
            user_id = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('id')
            
            if user_id:
                user = await UserSourceSchema.get(user_id)
                if user:
                    return user
        except JWTError as e:
            raise DecodeException()
    return None

