from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.password import get_password_hash
from asyncpg.exceptions import UniqueViolationError
from .authenticate_user import authenticate_user
from lib.security.jwt.token import create_access_token, get_current_user
from .exceptions import UniqueExecption, InvalidUser

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    
    payload = data.dict(exclude={'user_type'})

    payload["password"] = get_password_hash(payload.get("password", None))

    try:
        user = UserSourceSchema(
            **payload
        )
        await user.insert()

        return user.get_response()
    except UniqueViolationError as uniq:
        raise UniqueExecption()


@router.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(email=form_data.username, password=form_data.password)
    print(user)
    if user:
        token = create_access_token(user.dict())
        if token:
            return {"access_token": token, "token_type": "bearer"}
    else:
        raise InvalidUser()

@router.get("/login")
async def login(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token=token)
    if user:
        return user