from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.password import get_password_hash
from lib.security.jwt.token import get_current_user
from asyncpg.exceptions import UniqueViolationError
from .exceptions import UniqueExecption
from modules.auth.views import oauth2_scheme

router = APIRouter()


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    payload = data.dict(exclude={'user_type'})

    payload['password'] = get_password_hash(payload.get('password', None))

    try:
        user = UserSourceSchema(
            **payload
        )
        await user.insert()
        
        return user.get_response()
    except UniqueViolationError as uniq:
        raise UniqueExecption()


@router.delete("/delete", status_code=200)
async def delete(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token=token)
    if user:
        if await user.delete():
            return {"message": "ok"}
    
    return JSONResponse(
        content={
            "message": "This account does not exist"
        },
        status_code=status.HTTP_404_NOT_FOUND
    )
