from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer 
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.password import get_password_hash
from asyncpg.exceptions import UniqueViolationError
from lib.security.jwt.token import get_current_user
from .exceptions import UniqueExecption


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


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



@router.get('/login')
async def login(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token=token)
    if user:
        return user
