from fastapi import HTTPException

class UniqueExecption(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Entry already exists'}, status_code=409)
