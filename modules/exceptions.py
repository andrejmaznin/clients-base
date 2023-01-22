from fastapi import HTTPException


class EntityNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Entity does not exist'}, status_code=404)
