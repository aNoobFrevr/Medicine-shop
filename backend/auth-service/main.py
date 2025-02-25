from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
from common.logger import setup_logger

logger = setup_logger("auth_service")

app = FastAPI(title="Authentication Service")

# Connect to Redis for caching tokens
r = redis.Redis(host="redis", port=6379, decode_responses=True)

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(req: LoginRequest):
    logger.info("Login attempt for %s", req.email)
    # Dummy authentication logic
    if req.email == "user@example.com" and req.password == "password":
        token = "dummy-token"
        r.set(req.email, token)
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
