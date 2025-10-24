from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class Event(BaseModel):
    topic: str
    event_id: str
    timestamp: datetime
    source: str
    payload: Dict[str, Any]