from fastapi import APIRouter
from .schemas.request import OccRequestSchema
from .schemas.response import OccResponseSchema, ListOccResponseSchema
from .schemas.source import OccSourceSchema
from asyncpg.exceptions import UniqueViolationError
from modules.user.exceptions import UniqueException, EntityNotFoundException

router = APIRouter()

@router.post('/create', response_model=OccResponseSchema)
async def create(data: OccRequestSchema):
    payload = data.dict()
    try:
        occ = OccSourceSchema(**payload)

        await occ.insert()
        return occ.get_response()
    except UniqueViolationError as uniq:
        raise UniqueException()


@router.delete('/delete')
async def delete(data: OccRequestSchema):
    occ = await OccSourceSchema.get_by_occ(data.occupation)
    if occ:
        if await occ.delete():
            return {'message': 'ok'}
    
    raise EntityNotFoundException()


@router.get('/', response_model=ListOccResponseSchema)
async def get_all():
    occ = await OccSourceSchema.get_all()
    return occ