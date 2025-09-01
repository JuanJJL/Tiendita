from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Tiendita JSR")

# Dependencia de sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/personas/", response_model=schemas.Persona)
def crear_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    return crud.crear_persona(db, persona)

@app.post("/productos/", response_model=schemas.Producto)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.Producto])
def listar_productos(db: Session = Depends(get_db)):
    return crud.listar_productos(db)
