from fastapi import APIRouter
from app.modules.doors_windows.schemas import DoorsWindowsCreate, DoorsWindowsUpdate

router = APIRouter()


@router.get("/")
def list_doors_windows():
    return {"message": "List all doors & windows records"}


@router.get("/{id}")
def get_doors_windows(id: int):
    return {"message": f"Get doors & windows {id}"}


@router.post("/")
def create_doors_windows(payload: DoorsWindowsCreate):
    return {"message": "Create doors & windows record"}


@router.put("/{id}")
def update_doors_windows(id: int, payload: DoorsWindowsUpdate):
    return {"message": f"Update doors & windows {id}"}


@router.delete("/{id}")
def delete_doors_windows(id: int):
    return {"message": f"Delete doors & windows {id}"}
