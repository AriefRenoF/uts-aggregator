from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import Event
from .event_processor import EventProcessor

app = FastAPI()
processor = EventProcessor()

@app.on_event("startup")
async def startup_event():
    from .database import init_db
    init_db()

@app.post("/publish")
async def publish(events: List[Event]):
    await processor.publish(events)
    return {"message": "Events processed"}

@app.get("/events")
async def get_events(topic: str):
    events = processor.get_processed_events()
    return [event for event in events if event[0] == topic]

@app.get("/stats")
async def get_stats():
    return processor.get_stats()