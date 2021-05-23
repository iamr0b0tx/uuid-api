from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UUIDSchema(BaseModel):
    uuid: str
    timestamp: Optional[datetime]

    class Config:
        orm_mode = True
