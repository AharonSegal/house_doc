from pydantic import BaseModel


class PhotoBase(BaseModel):
    room: str
    photo_url: str
    description: str = None
    taken_at: str = None


class PhotoCreate(PhotoBase):
    pass


class PhotoUpdate(PhotoBase):
    pass
