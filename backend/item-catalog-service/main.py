from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("item_catalog_service")

app = FastAPI(title="Item Catalog Service")

@app.get("/items")
async def list_items():
    logger.info("Listing items")
    return [{"item_id": 1, "name": "Aspirin", "price": 9.99}]
