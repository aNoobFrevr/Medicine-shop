from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("customer_connect_service")

app = FastAPI(title="Customer Connect Service")

@app.get("/connect")
async def get_connections():
    logger.info("Fetching customer connections")
    return {"connections": []}
