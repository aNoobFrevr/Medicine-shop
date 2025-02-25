from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("customer_profile_service")

app = FastAPI(title="Customer Profile Service")

@app.get("/profile/{customer_id}")
async def get_profile(customer_id: int):
    logger.info("Fetching profile for customer %d", customer_id)
    return {"customer_id": customer_id, "profile": "Sample profile data"}
