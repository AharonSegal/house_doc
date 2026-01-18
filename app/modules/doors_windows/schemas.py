from pydantic import BaseModel


class DoorsWindowsBase(BaseModel):
    room: str
    type: str  # door/window
    model: str
    material: str
    dimensions: str
    manufacturer: str


class DoorsWindowsCreate(DoorsWindowsBase):
    pass


class DoorsWindowsUpdate(DoorsWindowsBase):
    pass
