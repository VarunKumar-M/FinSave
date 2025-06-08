
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/auth/health")
def health_check():
    return {"status": "auth service is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
