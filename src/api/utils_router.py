import logging

from fastapi import APIRouter, File, UploadFile, HTTPException


logger = logging.getLogger()

router = APIRouter()

IMAGES = {}


@router.get("/heartbeat", description="Checks that the microservice is still up and running.")
async def heartbeat() -> dict:
    """Endpoint for checking the status of the microservice.
    """

    logger.info("Check that the microservice is up and running")
    return {}

