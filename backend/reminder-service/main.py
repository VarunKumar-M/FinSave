
from fastapi import FastAPI

app = FastAPI()

@app.get("/reminders/health")
def health_check():
    return {"status": "reminder service is running"}
