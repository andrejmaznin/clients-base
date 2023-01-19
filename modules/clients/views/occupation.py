from fastapi import APIRouter, Depends
from ..schemas.occupation.request import OccRequestSchema
from ..schemas.occupation.response import OccResponseSchema, ListOccResponseSchema
from ..schemas.occupation.source import OccSourceSchema
from asyncpg.exceptions import UniqueViolationError
from modules.user.exceptions import UniqueException
from modules.exceptions import EntityNotFoundException
from dependencies.admin_auth import admin_auth


router = APIRouter()

@router.post('/create', response_model=OccResponseSchema, dependencies=[Depends(admin_auth)])
async def create(data: OccRequestSchema):
    payload = data.dict()
    try:
        occ = OccSourceSchema(**payload)

        await occ.insert()
        return occ.get_response()
    except UniqueViolationError as uniq:
        raise UniqueException()


@router.delete('/delete', dependencies=[Depends(admin_auth)])
async def delete(data: OccRequestSchema):
    occ = await OccSourceSchema.get_by_occ(data.occupation)
    if occ:
        if await occ.delete():
            return {'message': 'ok'}
    
    raise EntityNotFoundException()


@router.get('/', response_model=ListOccResponseSchema)
async def get_all():
    return await OccSourceSchema.get_all()
    


@router.get('/hint/{hint}', response_model=ListOccResponseSchema)
async def hint(hint: str):
    return await OccSourceSchema.get_with_hint(hint)
    


