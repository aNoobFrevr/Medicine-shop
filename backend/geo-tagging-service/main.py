from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("geo_tagging_service")

app = FastAPI(title="Geo-Tagging Service")

@app.get("/locations")
async def get_locations():
    logger.info("Fetching locations")
    return {"locations": []}
