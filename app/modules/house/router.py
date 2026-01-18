from fastapi import APIRouter
from app.modules.house.schemas import HouseCreate, HouseUpdate

router = APIRouter()


@router.get("/")
def list_houses():
    return {"message": "List all houses"}


@router.get("/{id}")
def get_house(id: int):
    return {"message": f"Get house {id}"}


@router.post("/")
def create_house(payload: HouseCreate):
    return {"message": "Create house"}


@router.put("/{id}")
def update_house(id: int, payload: HouseUpdate):
    return {"message": f"Update house {id}"}


@router.delete("/{id}")
def delete_house(id: int):
    return {"message": f"Delete house {id}"}
