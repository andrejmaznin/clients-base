from asyncpg.exceptions import UniqueViolationError
<< << << < HEAD

from lib.security.passwords import get_password_hash
== == == =
from fastapi import APIRouter

from lib.security.password import get_password_hash
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from .exceptions import UniqueExecption
>> >> >> > auth

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

    except UniqueViolationError:
        raise UniqueExecption()
