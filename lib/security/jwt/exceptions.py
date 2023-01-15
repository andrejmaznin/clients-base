from fastapi import Request, status
from fastapi.responses import JSONResponse


class DecodeException(Exception):
    pass


async def decode_exception_handler(request: Request, exc: DecodeException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "Invalid token"}
    )
