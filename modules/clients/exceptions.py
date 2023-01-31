from fastapi import HTTPException


class OccNotExistException(HTTPException):
    def __init__(self,) -> None:
        super().__init__(status_code=404, detail={'error': 'Occupation not in DB. Use /client/occupation/'})
