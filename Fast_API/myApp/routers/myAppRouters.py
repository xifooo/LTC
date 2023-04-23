from fastapi import APIRouter

router1 = APIRouter()
router2 = APIRouter()

@router1.get("/")
async def getAll():
    return {"message": "all"}

@router1.get("/{note_id}")
async def getOne():
    return {"message": "all"}
    
@router2.get("/")
async def getAll():
    return {"message": "all"}

@router2.get("/{note_id}")
async def getOne():
    return {"message": "all"}

