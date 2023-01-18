from fastapi import APIRouter

from modules.occupation.views import router as occ_router

router = APIRouter()
router.include_router(occ_router)
