from fastapi import HTTPException


class InvalidUser(HTTPException):
    def __init__(self):
        super().__init__(detail={'error': 'Invalid password or email'}, status_code=401)