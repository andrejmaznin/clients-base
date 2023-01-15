from fastapi import HTTPException


class InvalidCredentials(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Invalid password or email'}, status_code=401)
