from datetime import datetime, date
from pydantic import BaseModel


class EventInfo(BaseModel):
    id: int
    name: str
    startDate: date
    endDate: date
    longitude: float
    latitude: float
    imageUrl: str
    categories: str
    habitantes: float

    distance: float | None = None
