from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    role: str  # contractor, architect, designer, etc.
    phone: str = None
    email: str = None


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    pass
