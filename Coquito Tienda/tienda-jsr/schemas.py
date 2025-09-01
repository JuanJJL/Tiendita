from pydantic import BaseModel
from typing import Optional

class PersonaBase(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int
    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    class Config:
        orm_mode = True
