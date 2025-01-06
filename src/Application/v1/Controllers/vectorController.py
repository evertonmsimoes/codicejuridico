from fastapi import APIRouter, HTTPException
from src.Core.Schemas.Requests import UpdateIndex


router = APIRouter(prefix="/v1")


@router.post("/create_index")
async def createIndex(request: UpdateIndex):
    try:
        pass
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=str(e)
        )
