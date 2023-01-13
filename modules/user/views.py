from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema
from lib.security.password.password_crypt import get_password_hash
from asyncpg.exceptions import UniqueViolationError

router = APIRouter()

class CreateUserResponseSchema:
    pass


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    
    payload = data.dict()

    payload["password"] = get_password_hash(payload.get("password", None))

    try:
        user = UserSourceSchema(
            **payload
        )
        await user.insert()

        return user.get_response()
    except UniqueViolationError as uniq:

        return JSONResponse(content=uniq.as_dict().get("detail"), status_code=status.HTTP_409_CONFLICT)
