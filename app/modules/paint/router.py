from fastapi import APIRouter
from app.modules.paint.schemas import PaintCreate, PaintUpdate

router = APIRouter()


@router.get("/")
def list_paints():
    return {"message": "List all paint records"}


@router.get("/{id}")
def get_paint(id: int):
    return {"message": f"Get paint {id}"}


@router.post("/")
def create_paint(payload: PaintCreate):
    return {"message": "Create paint record"}


@router.put("/{id}")
def update_paint(id: int, payload: PaintUpdate):
    return {"message": f"Update paint {id}"}


@router.delete("/{id}")
def delete_paint(id: int):
    return {"message": f"Delete paint {id}"}
