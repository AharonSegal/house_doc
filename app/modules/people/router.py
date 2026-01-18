from fastapi import APIRouter
from app.modules.people.schemas import PersonCreate, PersonUpdate

router = APIRouter()


@router.get("/")
def list_people():
    return {"message": "List all people"}


@router.get("/{id}")
def get_person(id: int):
    return {"message": f"Get person {id}"}


@router.post("/")
def create_person(payload: PersonCreate):
    return {"message": "Create person"}


@router.put("/{id}")
def update_person(id: int, payload: PersonUpdate):
    return {"message": f"Update person {id}"}


@router.delete("/{id}")
def delete_person(id: int):
    return {"message": f"Delete person {id}"}
