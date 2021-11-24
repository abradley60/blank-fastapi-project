import os

import uvicorn
from src.api import app  # noqa
from src.api.setup_logging import setup_logging

# config = setup_logging(path="/opt/working/logging.yaml") #EC2
config = setup_logging(path="logging.yaml")


# Initialize the FastAPI application
if __name__ == "__main__":
    uvicorn.run("api:app", port=5555, host="0.0.0.0", reload=True, log_config=config)
    # uvicorn.run("api:app", port=int(os.environ["FASTAPI_PORT"]), host="0.0.0.0", reload=os.environ["DEBUG"], log_config=config) #EC2
