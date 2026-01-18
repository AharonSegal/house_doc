from pydantic import BaseModel


class PaintBase(BaseModel):
    room: str
    area_type: str  # interior/exterior
    brand: str
    color_code: str
    finish: str  # matte, semi-gloss, etc.


class PaintCreate(PaintBase):
    pass


class PaintUpdate(PaintBase):
    pass
