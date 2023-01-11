from fastapi import APIRouter

from modules.user.schemas.request import CreateUserRequestSchema
from modules.user.schemas.response import UserResponseSchema
from modules.user.schemas.source import UserSourceSchema

router = APIRouter()


class CreateUserResponseSchema:
    pass


@router.post('/register', response_model=UserResponseSchema)
async def register(data: CreateUserRequestSchema):
    user = UserSourceSchema(
        **data.dict(exclude={'user_type'})
    )
    await user.insert()

    return user.get_response()
