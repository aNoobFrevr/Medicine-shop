from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("inventory_service")

app = FastAPI(title="Inventory Service")

@app.get("/inventory")
async def get_inventory():
    logger.info("Fetching inventory")
    return {"inventory": []}
