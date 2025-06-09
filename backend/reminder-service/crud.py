from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Reminder
from schemas import ReminderCreate

async def create_reminder(db: AsyncSession, reminder: ReminderCreate):
    db_reminder = Reminder(**reminder.dict())
    db.add(db_reminder)
    await db.commit()
    await db.refresh(db_reminder)
    return db_reminder

async def get_reminders(db: AsyncSession, user_id: int = None):
    query = select(Reminder)
    if user_id is not None:
        query = query.where(Reminder.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()
