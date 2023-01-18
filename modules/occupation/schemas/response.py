from pydantic import BaseModel

class OccResponseSchema(BaseModel):
    id: int
    occ: str
