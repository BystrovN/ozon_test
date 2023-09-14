from datetime import datetime

from pydantic import BaseModel


class OzonPingRequest(BaseModel):
    message_type: str
    time: datetime


class OzonUser(BaseModel):
    id: int
    type: str


class OzonBaseRequest(BaseModel):
    message_type: str
    chat_id: str
    chat_type: str
    message_id: str
    created_at: datetime
    user: OzonUser
    seller_id: int


class OzonNewMsgRequest(OzonBaseRequest):
    data: list[str]


class OzonMsgReadRequest(OzonBaseRequest):
    last_read_message_id: str
