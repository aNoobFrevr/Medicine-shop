from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("order_management_service")

app = FastAPI(title="Order Management Service")

@app.post("/orders")
async def create_order(order: dict):
    logger.info("Creating order: %s", order)
    return {"order_id": 123, "status": "created"}
