from sqlalchemy.orm import Session
from . import models, schemas

def create_transaction(db: Session, txn: schemas.TransactionCreate):
    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def delete_transaction(db: Session, txn_id: int):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    if txn:
        db.delete(txn)
        db.commit()
    return txn