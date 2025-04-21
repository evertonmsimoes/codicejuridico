from fastapi import APIRouter, HTTPException
from src.Core.Schemas.Requests import UpdateIndex


router = APIRouter(prefix="/v1")


@router.post("/create_index")
async def createIndex(request: UpdateIndex):
    try:
        
        return {
            "index_name": request.index_name,
            "chunk_size": request.chunk_size,
            "chunk_overlap": request.chunk_overlap,
            "reader_type": request.reader_type
        }
    
    except Exception as e:
        raise  HTTPException(
            status_code=500,
            detail=str(e)
        )
