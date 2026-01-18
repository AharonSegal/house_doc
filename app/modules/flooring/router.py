from fastapi import APIRouter
from app.modules.flooring.schemas import FlooringCreate, FlooringUpdate

router = APIRouter()


@router.get("/")
def list_flooring():
    return {"message": "List all flooring records"}


@router.get("/{id}")
def get_flooring(id: int):
    return {"message": f"Get flooring {id}"}


@router.post("/")
def create_flooring(payload: FlooringCreate):
    return {"message": "Create flooring record"}


@router.put("/{id}")
def update_flooring(id: int, payload: FlooringUpdate):
    return {"message": f"Update flooring {id}"}


@router.delete("/{id}")
def delete_flooring(id: int):
    return {"message": f"Delete flooring {id}"}
