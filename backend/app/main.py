import logging
import pytz
from datetime import datetime

from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool

from .schemas import OzonMsgReadRequest, OzonNewMsgRequest, OzonPingRequest

APP_VERSION = "v0.1"
APP_NAME = "chat2desk"
app = FastAPI()

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@app.middleware("http")
async def log_request(request: Request, call_next):
    logger.info(
        f"Request: {request.method} url - {request.url} params - {request.query_params}"
    )

    response = await call_next(request)

    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    logger.info(
        f"Response: status - {response.status_code}, body {response_body[0].decode()}"
    )
    logger.info("\n")

    return response


@app.post(path="/ozon")
async def test(data: OzonPingRequest | OzonNewMsgRequest | OzonMsgReadRequest):
    logger.info(f"request body - {data}")
    if data.message_type == "TYPE_PING":
        return {
            "version": APP_VERSION,
            "name": APP_NAME,
            "time": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    return {"result": True}
