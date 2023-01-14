from jose import JWTError, jwt
from os import getenv
from tables import user
from lib.postgresql import get_connection
from .schemas.user import User
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


async def get_current_user(token: str) -> None | User:
    if SECRET_KEY:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
            query = user.select().where(
                user.c.id == payload.get('id'), 
                user.c.email == payload.get('email'),
                user.c.phone_number == payload.get('phone_number'),
            )
            
            entity = await get_connection().fetch_one(query)
            if entity:
                return User.from_orm(entity)
        except JWTError as e:
            raise DecodeException()
    return None

