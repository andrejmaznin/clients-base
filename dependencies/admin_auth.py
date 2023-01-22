from fastapi import Header, HTTPException
import os


async def admin_auth(
        admin_secret: str = Header(
            description="Admin secret key",
            example="Admin Key"
        )):
    x, key = admin_secret.split()
    if x.lower() != "admin" or key != os.getenv('ADMIN_SECRET_KEY'):
        raise HTTPException(status_code=403, detail='admin-secret header invalid')
