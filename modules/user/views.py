from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
<<<<<<< Updated upstream
from .services import get_password_hash
=======
from lib.security import password
>>>>>>> Stashed changes
from asyncpg.exceptions import UniqueViolationError
from lib.postgresql import get_connection
from tables import user as user_table
from lib.security.jwt.token import create_access_token


router = APIRouter()


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    
    payload = data.dict(exclude={'user_type'})

    payload["password"] = password.get_password_hash(payload.get("password", None))

    try:
        user = UserSourceSchema(
            **payload
        )
        await user.insert()

        return user.get_response()
    except UniqueViolationError as uniq:

        return JSONResponse(content=uniq.as_dict().get("detail"), status_code=status.HTTP_409_CONFLICT)


@router.get("/auth")
async def auth(email: str, password: str):
    query = user_table.select().where(user_table.c.email == email)
    user = await get_connection().fetch_one(query=query)
    if user:
        user = dict(user._mapping)
        password_hash = user.get("password")
        if password_hash != None and verify_password(password, password_hash) == True:
            token = create_access_token(user)
            if token:
                return JSONResponse({"token": token})