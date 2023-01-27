from pydantic import BaseModel
from uuid import UUID


class DeleteClientResponseScheme(BaseModel):
    id: UUID
    succses: bool