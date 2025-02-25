from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("user_account_service")

app = FastAPI(title="User Account Service")

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    logger.info("Fetching user %d", user_id)
    return {"user_id": user_id, "name": "John Doe"}
