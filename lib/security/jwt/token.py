from jose import JWTError, jwt
from os import getenv
from modules.user.schemas.source import UserSourceSchema
from .exceptions import DecodeException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


ALGORITHM = 'HS256'
SECRET_KEY = getenv('SECRET_KEY')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


def create_access_token(data: dict) -> str | None:
    data['id'] = str(data['id'])
    del data['birthdate']
    if SECRET_KEY:
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    return None


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSourceSchema | None:
    if SECRET_KEY:
        try:
            user_id = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('id')    
        except JWTError as e:
            raise DecodeException()
        
        if user_id:
            user = await UserSourceSchema.get(user_id)
            if user:
                return user
    return None

