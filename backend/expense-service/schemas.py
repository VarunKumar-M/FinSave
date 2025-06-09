from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class Expense(ExpenseCreate):
    id: int
    date: datetime

    class Config:
        orm_mode = True
