from fastapi import APIRouter, Depends
from lib.security.jwt.token import get_current_user
from modules.user.schemas.source import UserSourceSchema
from modules.clients.schemas.clients.source import ClientSourceSchema
from modules.clients.schemas.clients.request import ClientRequestSchema
from asyncpg.exceptions import UniqueViolationError, ForeignKeyViolationError
from modules.exceptions import UniqueException
from ..exceptions import OccNotExistException
from fastapi.exceptions import RequestValidationError


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
