
from fastapi import FastAPI

app = FastAPI()

@app.get("/expenses/health")
def health_check():
    return {"status": "expense service is running"}
