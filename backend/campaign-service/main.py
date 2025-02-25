from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("campaign_service")

app = FastAPI(title="Campaign Service")

@app.get("/campaigns")
async def get_campaigns():
    logger.info("Fetching campaigns")
    return {"campaigns": []}
