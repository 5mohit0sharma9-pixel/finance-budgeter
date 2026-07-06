from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    title: str
    amount: float
    category: str
    type: str
    date: date

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True