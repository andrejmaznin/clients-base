
from pydantic import BaseModel
from .response import OccResponseSchema
from lib.postgresql.mixin import PostgreSQLMixin
from lib.postgresql.utils import postgresql
from tables import occupation


@postgresql(table=occupation)
class OccSourceSchema(PostgreSQLMixin, BaseModel):
    id: int | None
    occ: str

    def get_response(self):
        return OccResponseSchema(
            id=self.id, 
            occ=self.occ
        )