from fastapi import APIRouter

router = APIRouter()

@router.get("/path2")
async def get_data():
    pass