from pydantic import BaseModel

class OccRequestSchema(BaseModel):
    occupation: str

    class Config:
        schema_extra = {
            "example": {
                "occupation": "Doctor"
            }
        }