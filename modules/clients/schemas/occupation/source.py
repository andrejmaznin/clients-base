
from pydantic import BaseModel
from .response import OccResponseSchema
from lib.postgresql.mixin import PostgreSQLMixin
from lib.postgresql.utils import postgresql
from lib.postgresql import get_connection
from tables import occupation


@postgresql(table=occupation)
class OccSourceSchema(PostgreSQLMixin, BaseModel):
    id: int | None
    occupation: str

    def get_response(self):
        return OccResponseSchema(
            id=self.id, 
            occupation=self.occupation
        )
    
    @classmethod
    async def get_by_occ(cls, occ: str):
        query = cls.table.select().where(cls.table.c.occupation==occ)
        entity = await get_connection().fetch_one(query=query)
        if entity:
            return cls(**entity)

    @classmethod 
    async def get_all(cls):
        query = cls.table.select()
        entity = await get_connection().fetch_all(query=query)
        if entity:
            return entity
    

    @classmethod 
    async def get_with_hint(cls, hint: str):
        entity = await get_connection().fetch_all(query='SELECT id, occupation, occupation <-> :hint AS dist FROM occupation ORDER BY dist LIMIT 10', values={'hint': hint})
        if entity:
            return entity
    