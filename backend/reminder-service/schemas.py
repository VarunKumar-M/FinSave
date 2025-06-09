from pydantic import BaseModel
from datetime import datetime

class ReminderCreate(BaseModel):
    user_id: int
    message: str
    remind_at: datetime

class ReminderOut(ReminderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
from pydantic import BaseModel
from datetime import datetime

class ReminderCreate(BaseModel):
    user_id: int
    message: str
    remind_at: datetime

class ReminderOut(ReminderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
