from fastapi import APIRouter
from app.modules.appliances.schemas import ApplianceCreate, ApplianceUpdate

router = APIRouter()


@router.get("/")
def list_appliances():
    return {"message": "List all appliances records"}


@router.get("/{id}")
def get_appliance(id: int):
    return {"message": f"Get appliance {id}"}


@router.post("/")
def create_appliance(payload: ApplianceCreate):
    return {"message": "Create appliance record"}


@router.put("/{id}")
def update_appliance(id: int, payload: ApplianceUpdate):
    return {"message": f"Update appliance {id}"}


@router.delete("/{id}")
def delete_appliance(id: int):
    return {"message": f"Delete appliance {id}"}
