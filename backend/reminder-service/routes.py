from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import ReminderCreate, ReminderOut
from crud import create_reminder, get_reminders
from typing import List, Optional

router = APIRouter()

@router.post("/", response_model=ReminderOut)
async def add_reminder(reminder: ReminderCreate, db: AsyncSession = Depends(get_db)):
    return await create_reminder(db, reminder)

@router.get("/", response_model=List[ReminderOut])
async def list_reminders(user_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    return await get_reminders(db, user_id)
