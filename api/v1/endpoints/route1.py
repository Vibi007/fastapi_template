from fastapi import APIRouter

router = APIRouter()

@router.get("/path1")
async def get_data():
    pass