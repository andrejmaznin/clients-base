from fastapi import APIRouter, Depends
from modules.user.schemas.request import CreateUserRequestSchema, UpdateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.passwords import get_password_hash
from lib.security.jwt.token import get_current_user
from asyncpg.exceptions import UniqueViolationError
from modules.exceptions import UniqueException
from modules.exceptions import EntityNotFoundException


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
    except UniqueViolationError:
        raise UniqueException()


@router.delete('/delete', status_code=200)
async def delete(user: UserSourceSchema | None = Depends(get_current_user)):
    if user:
        if await user.delete():
            return {'message': 'ok'}
    
    raise EntityNotFoundException()


@router.put('/update', response_model=UserResponseSchema, status_code=200)
async def update(data: UpdateUserRequestSchema, user: UserSourceSchema | None =  Depends(get_current_user)):
    payload = data.dict(exclude_none=True, exclude_unset=True)
    password = payload.get('password', None)
    if password:
        payload['password'] = get_password_hash(password)

    
    if user:
        u = await user.update(**payload)
        return u.get_response()
        
    raise UserNotFoundException()
