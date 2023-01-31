from fastapi import HTTPException


class EntityNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Entity does not exist'}, status_code=404)


class UniqueException(HTTPException):
    def __init__(self, entity: str):
        super().__init__(detail={'error': f'{entity} already exists'}, status_code=409)
