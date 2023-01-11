from sqlalchemy import Table

from lib.postgresql import database


def transaction(func):
    async def wrapper(self, *args, **kwargs):
        async with database.transaction():
            return await func(self, *args, **kwargs)

    return wrapper


def postgresql(table: Table):
    def wrap(schema_cls):
        setattr(schema_cls, 'table', table)
        return schema_cls

    return wrap
