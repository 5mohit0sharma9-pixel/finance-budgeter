from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add", response_model=schemas.TransactionResponse)
def add_transaction(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, txn)

@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@router.delete("/delete/{txn_id}")
def delete(txn_id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db, txn_id)