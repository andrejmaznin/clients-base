from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from lib.security.jwt.token import create_access_token
from .authenticate_user import authenticate_user
from .exceptions import InvalidUser

router = APIRouter()


@router.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(email=form_data.username, password=form_data.password)
    if user:
        token = create_access_token(user.dict())
        if token:
            return {'access_token': token, 'token_type': 'bearer'}
    else:
        raise InvalidUser()