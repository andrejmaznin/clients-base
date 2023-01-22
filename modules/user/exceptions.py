from fastapi import HTTPException

class UniqueException(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Entity already exists'}, status_code=409)


