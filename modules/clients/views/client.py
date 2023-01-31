from fastapi import APIRouter, Depends, Body
from lib.security.jwt.token import get_current_user
from modules.user.schemas.source import UserSourceSchema
from modules.clients.schemas.clients.source import ClientSourceSchema
from modules.clients.schemas.clients.request import *
from modules.clients.schemas.clients.response import *
from asyncpg.exceptions import UniqueViolationError, ForeignKeyViolationError
from modules.exceptions import UniqueException, EntityNotFoundException
from ..exceptions import OccNotExistException
from fastapi.exceptions import RequestValidationError
from ..schemas.hint.source import HintClientSourceSchema
from uuid import UUID
from ..schemas.hint.response import HintClientResponseSchema


router = APIRouter()


@router.post('/create', response_model=list[ClientSourceSchema],status_code=201)
async def create(clients_data: list[ClientRequestSchema], user: UserSourceSchema | None = Depends(get_current_user)):
    clients = []
    valid_erorrs = []

    for client_data in clients_data:
        payload = client_data.dict()
        try:
            client = ClientSourceSchema(user=user.id, **payload)
            erorrs = await client.valid()
            if len(erorrs) == 0:
                await client.insert()
                clients.append(client)

            valid_erorrs.extend(erorrs)
        except ForeignKeyViolationError:
            raise OccNotExistException()
        except UniqueViolationError:
            raise UniqueException(client.email)
    if valid_erorrs:
        raise RequestValidationError(errors=valid_erorrs)
    return clients



@router.put('/update/{uuid}', response_model=ClientSourceSchema)
async def update(client_data: UpdateClientRequestSchema, uuid: UUID, user: UserSourceSchema | None = Depends(get_current_user)):
    if user:
        payload = client_data.dict(exclude_none=True, exclude_unset=True)
        client = await ClientSourceSchema.get_by_user(user_id=user.id, client_id=uuid)
        if client:
            try:
                return await client.update(**payload)
            except ForeignKeyViolationError:
                raise OccNotExistException()
    raise EntityNotFoundException()


@router.delete('/delete', response_model=list[DeleteClientResponseScheme])
async def delete(payload: DeleteClientRequestSchema, user: UserSourceSchema | None = Depends(get_current_user)):
    succesed = []
    if user is not None and len(payload.id) != 0:
        for client_id in payload.id:
            client = await ClientSourceSchema.get_by_user(user_id=user.id, client_id=client_id)
            if client:
                succesed.append(
                    DeleteClientResponseScheme(
                        id=client.id, 
                        succses=await client.delete()
                        )
                )
        return succesed

    raise EntityNotFoundException()



@router.post('/hint', response_model=HintClientResponseSchema)
async def hint(hint_client: HintClientSourceSchema, user: UserSourceSchema | None = Depends(get_current_user)):
    if user:
        return await hint_client.get_hint(user_id=user.id)
