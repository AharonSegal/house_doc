from fastapi import APIRouter
from app.modules.files.schemas import FileCreate, FileUpdate

router = APIRouter()


@router.get("/")
def list_files():
    return {"message": "List all files"}


@router.get("/{id}")
def get_file(id: int):
    return {"message": f"Get file {id}"}


@router.post("/")
def create_file(payload: FileCreate):
    return {"message": "Create file"}


@router.put("/{id}")
def update_file(id: int, payload: FileUpdate):
    return {"message": f"Update file {id}"}


@router.delete("/{id}")
def delete_file(id: int):
    return {"message": f"Delete file {id}"}
