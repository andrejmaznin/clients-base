from fastapi import Header, HTTPException


async def admin_auth(admin_secret: str = Header()):
    return admin_secret