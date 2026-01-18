from pydantic import BaseModel


class ApplianceBase(BaseModel):
    room: str
    appliance_type: str  # washer, fridge, oven, etc.
    brand: str
    model: str
    serial_number: str = None
    warranty_expiry: str = None


class ApplianceCreate(ApplianceBase):
    pass


class ApplianceUpdate(ApplianceBase):
    pass
