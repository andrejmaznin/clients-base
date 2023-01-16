from fastapi import HTTPException

class UniqueExecption(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Entity already exists'}, status_code=409)
