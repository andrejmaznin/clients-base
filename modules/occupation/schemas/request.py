from pydantic import BaseModel

class OccRequestSchema(BaseModel):
    occ: str

    class Config:
        schema_extra = {
            "example": {
                "occ": "Doctor"
            }
        }