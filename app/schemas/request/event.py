from datetime import datetime, date
from pydantic import BaseModel


class EventRequest(BaseModel):
    name: str
    startDate: date
    endDate: date
    longitude: float
    imageUrl: str
    categories: str
    habitantes: float
