from fastapi import FastAPI
from routes import router
from database import create_tables

app = FastAPI(title="Reminder Service")
app.include_router(router, prefix="/reminders")

@app.on_event("startup")
async def startup_event():
    await create_tables()
