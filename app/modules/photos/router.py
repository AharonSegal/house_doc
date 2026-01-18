from fastapi import APIRouter
from app.modules.photos.schemas import PhotoCreate, PhotoUpdate

router = APIRouter()


@router.get("/")
def list_photos():
    return {"message": "List all photos"}


@router.get("/{id}")
def get_photo(id: int):
    return {"message": f"Get photo {id}"}


@router.post("/")
def create_photo(payload: PhotoCreate):
    return {"message": "Create photo"}


@router.put("/{id}")
def update_photo(id: int, payload: PhotoUpdate):
    return {"message": f"Update photo {id}"}


@router.delete("/{id}")
def delete_photo(id: int):
    return {"message": f"Delete photo {id}"}
