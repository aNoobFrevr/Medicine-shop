from fastapi import FastAPI, Request
import httpx
from common.logger import setup_logger

app = FastAPI(title="API Gateway")
logger = setup_logger("api_gateway")

# Example: Proxy login requests to the auth service
AUTH_SERVICE_URL = "http://auth-service:8000"

@app.post("/api/auth/login")
async def login(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/login", json=data)
    return response.json()

@app.get("/")
async def root():
    return {"message": "API Gateway is running"}
