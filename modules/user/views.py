from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from modules.user.schemas.request import CreateUserRequestSchema, UpdateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.password import get_password_hash
from lib.security.jwt.token import get_current_user
from asyncpg.exceptions import UniqueViolationError
from .exceptions import UniqueExecption
from modules.auth.views import oauth2_scheme
from .enums import BaseContent

router = APIRouter()


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    payload = data.dict()

    payload['password'] = get_password_hash(payload.get('password', None))

    try:
        user = UserSourceSchema(
            **payload
        )
        await user.insert()
        
        return user.get_response()
    except UniqueViolationError as uniq:
        raise UniqueExecption()


@router.delete('/delete', status_code=200)
async def delete(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token=token)
    if user:
        if await user.delete():
            return {'message': 'ok'}
    
    return JSONResponse(
        content=BaseContent.USER_NOT_EXIST.value,
        status_code=status.HTTP_404_NOT_FOUND
    )


@router.put('/update', response_model=UserResponseSchema, status_code=200)
async def update(data: UpdateUserRequestSchema, token: str = Depends(oauth2_scheme)):
    payload = data.dict(exclude_none=True)
    password = payload.get('password', None)
    if password:
        payload['password'] = get_password_hash(password)

    user = await get_current_user(token=token)
    if user:
        up = await user.update(payload)
        return up.get_response()
        

    return JSONResponse(
        content=BaseContent.USER_NOT_EXIST.value,
        status_code=status.HTTP_404_NOT_FOUND
    )