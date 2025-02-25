from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("ledger_service")

app = FastAPI(title="Ledger Service")

@app.get("/ledger")
async def get_ledger():
    logger.info("Fetching ledger")
    return {"ledger": "data"}
