# app/main.py - FastAPI application entry point
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My FastAPI App", version="1.0.0")

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", version="1.0.0")