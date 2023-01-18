from fastapi import APIRouter
from .schemas.request import OccRequestSchema
from .schemas.response import OccResponseSchema
from .schemas.source import OccSourceSchema
from asyncpg.exceptions import UniqueViolationError
from modules.user.exceptions import UniqueException

router = APIRouter()

@router.post('/create', response_model=OccResponseSchema)
async def create(data: OccRequestSchema):
    try:
        occ = OccSourceSchema(**data)

        await occ.insert()
        return occ.get_response()
    except UniqueViolationError as uniq:
        raise UniqueException()