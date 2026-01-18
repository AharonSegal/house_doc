from pydantic import BaseModel


class HouseBase(BaseModel):
    address: str
    year_built: int
    total_area: float


class HouseCreate(HouseBase):
    pass


class HouseUpdate(HouseBase):
    pass
