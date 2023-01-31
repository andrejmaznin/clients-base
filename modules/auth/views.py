from fastapi import APIRouter, Depends
from lib.security.jwt.token import create_access_token
from .internals import authenticate_user
from .exceptions import InvalidCredentials
from lib.security.jwt.token import get_current_user
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(email=form_data.username, password=form_data.password)
    if user:
        token = create_access_token(user.dict())
        if token:
            return {'access_token': token, 'token_type': 'bearer'}
    else:
        raise InvalidCredentials()


@router.get('/', response_model=UserResponseSchema)
async def login(user: UserSourceSchema | None = Depends(get_current_user)):
    if user:
        return user.get_response()

