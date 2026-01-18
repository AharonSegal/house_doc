from pydantic import BaseModel


class FlooringBase(BaseModel):
    room: str
    tile_name: str
    tile_model: str
    material: str
    manufacturer: str


class FlooringCreate(FlooringBase):
    pass


class FlooringUpdate(FlooringBase):
    pass
