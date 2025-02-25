from fastapi import FastAPI
from common.logger import setup_logger

logger = setup_logger("reporting_service")

app = FastAPI(title="Reporting Service")

@app.get("/reports")
async def get_reports():
    logger.info("Generating report")
    return {"report": "Sample analytics data"}
