from fastapi import APIRouter
from .views.occupation import router as occ_router
from .views.client import router as client_router


router = APIRouter()

router.include_router(occ_router, prefix='/occupation')
router.include_router(client_router)
