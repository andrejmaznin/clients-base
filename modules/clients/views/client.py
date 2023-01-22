from fastapi import APIRouter, Depends
from lib.security.jwt.token import get_current_user
from modules.user.schemas.source import UserSourceSchema
from modules.clients.schemas.clients.source import ClientSourceSchema
from modules.clients.schemas.clients.request import ClientRequestSchema
from asyncpg.exceptions import UniqueViolationError, ForeignKeyViolationError
from modules.exceptions import UniqueException
from ..exceptions import OccNotExistException


router = APIRouter()


@router.post('/create', response_model=ClientSourceSchema, status_code=201)
async def create(client_data: ClientRequestSchema, user: UserSourceSchema | None = Depends(get_current_user)):
	payload = client_data.dict()
	try:
		client = ClientSourceSchema(user=user.id, **payload)
		await client.insert()
		
		return client
	except ForeignKeyViolationError:
		raise OccNotExistException()
	except UniqueViolationError:
		raise UniqueException()