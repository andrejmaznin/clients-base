from typing import Union
from uuid import UUID

from pydantic import BaseModel

from lib.postgresql import database, get_connection
from lib.postgresql.utils import transaction

class PostgreSQLMixin(BaseModel):
    class Config:
        orm_mode = True

    @transaction
    async def insert(self):
        if self.id is None:
            query = self.table.insert()
            self.id = await get_connection().execute(
                query,
                self.dict(exclude={'id'})
            )
            return self

        query = self.table.update().where(self.table.c.id == self.id)
        await database.execute(
            query,
            {'id': self.id, **self.dict(exclude={'id'})}
        )
        return self

    @classmethod
    async def get(cls, id_: Union[UUID, str]):
        query = cls.table.select().where(cls.table.c.id == id_)
        entity = await get_connection().fetch_one(query)
        if entity is None:
            return None
        return cls(**entity)

    @transaction
    async def delete(self):
        query = self.table.delete().where(self.table.c.id == self.id)
        await get_connection().execute(query=query)
        return True

    @transaction
    async def update(self, **kwargs):
        query = self.table.update().where(self.table.c.id == self.id)
        await get_connection().execute(
            query=query,
            values=kwargs
        )
        entity = await get_connection().fetch_one(self.table.select().where(self.table.c.id == self.id))
        return self.from_orm(entity)
