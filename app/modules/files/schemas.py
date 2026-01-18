from pydantic import BaseModel
from datetime import date


class FileBase(BaseModel):
    title: str
    file_type: str  # permit, schematic, contract, etc.
    file_url: str
    note: str = None
    created_at: date = None


class FileCreate(FileBase):
    pass


class FileUpdate(FileBase):
    pass
