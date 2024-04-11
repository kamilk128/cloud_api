import math
from typing import List
from fastapi import APIRouter, HTTPException, status
from app.models.events import Events
from app.schemas.request.event import EventRequest
from app.schemas.response.event import (
    EventInfo,
    EventInfo,
)
import math

router = APIRouter(
    prefix="",
    tags=["events"],
)


@router.get("/objects", response_model=List[EventInfo])
async def get_events_all():
    return await Events.all()


@router.get("/object", response_model=List[EventInfo])
async def get_events_by_name(name=None):
    return await Events.filter(name=name)


@router.post("/object", response_model=EventInfo, status_code=status.HTTP_201_CREATED)
async def create_event(event_data: EventRequest):
    return await Events.create(**event_data.model_dump())


@router.put("/update", response_model=EventInfo)
async def update_event(
    id: int,
    event_data: EventRequest,
):
    event: Events = await Events.filter(id=id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    for key, value in event_data.model_dump().items():
        setattr(event, key, value)

    await event.save()

    return event


@router.get("/stats", response_model=List[EventInfo])
async def get_events_all(latitude: float, longitude: float):
    location = [latitude, longitude]
    events = await Events.all()
    distances = {}
    events.sort(
        key=lambda event: distance_between(
            event, [event.latitude, event.longitude], location, distances
        )
    )

    event_info_list = [
        EventInfo(**event.__dict__, distance=distances[event.name]) for event in events
    ]
    # distance=distances[event.name]

    return event_info_list


def distance_between(event, marker1, marker2, distances):
    lat1 = math.radians(marker1[0])
    lat2 = math.radians(marker2[0])
    lng1 = math.radians(marker1[1])
    lng2 = math.radians(marker2[1])

    dlat = lat2 - lat1
    dlng = lng2 - lng1

    a = math.pow(math.sin(dlat / 2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(
        math.sin(dlng / 2), 2
    )
    c = 2 * math.asin(math.sqrt(a))

    distances[event.name] = c * 6371

    return c * 6371
