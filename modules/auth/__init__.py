from fastapi import APIRouter

from modules.auth.views import router as auth_router

router = APIRouter()
router.include_router(auth_router)
