from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
