from fastapi import APIRouter
from .endpoints import route1,route2
router = APIRouter()

router.include_router(route1.router,tags=["route 1"])
router.include_router(route2.router,tags=["route 2"])