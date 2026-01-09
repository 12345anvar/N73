from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db_settings import SessionLocal, engine, Base
from core import tables
from crud import user as user_crud

tables.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Qarzlar Boshqaruvi")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Tizim ishlamoqda"}

@app.post("/add-debt")
def add_new_debt(ism: str, nomer: str, summa: int, turi: str, db: Session = Depends(get_db)):
    try:
        return user_crud.create_debt_manager(db, ism, nomer, summa, turi)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Xatolik yuz berdi: {str(e)}")

@app.get("/debts")
def list_debts(db: Session = Depends(get_db)):
    return user_crud.get_all_debts_manager(db)