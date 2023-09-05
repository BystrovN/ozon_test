from datetime import datetime
import pytz

from fastapi import FastAPI

from .schemas import OzonPingRequest, OzonNewMsgRequest, OzonMsgReadRequest

APP_VERSION = 'v0.1'
APP_NAME = 'chat2desk'
app = FastAPI()
current_datetime = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')


@app.post(path='/ozon')
def test(data: OzonPingRequest | OzonNewMsgRequest | OzonMsgReadRequest):
    if data.message_type == 'TYPE_PING':
        return {
            'version': APP_VERSION,
            'name': APP_NAME,
            'time': current_datetime,
        }
    return {'result': True}
