from collections import defaultdict
from typing import List
from .database import add_event, get_events
from .models import Event

class EventProcessor:
    def __init__(self):
        self.event_queue = []  # In-memory queue
        self.processed_events = set()  # Set for deduplication
        self.stats = {
            "received": 0,
            "unique_processed": 0,
            "duplicate_dropped": 0,
            "topics": set(),
            "uptime": 0,  # Placeholder for uptime logic
        }

    async def publish(self, events: List[Event]):
        for event in events:
            self.stats["received"] += 1
            if (event.topic, event.event_id) not in self.processed_events:
                if add_event(event.topic, event.event_id):
                    self.processed_events.add((event.topic, event.event_id))
                    self.stats["unique_processed"] += 1
                    self.stats["topics"].add(event.topic)
                else:
                    self.stats["duplicate_dropped"] += 1

    def get_stats(self):
        return {
            "received": self.stats["received"],
            "unique_processed": self.stats["unique_processed"],
            "duplicate_dropped": self.stats["duplicate_dropped"],
            "topics": list(self.stats["topics"]),
            "uptime": self.stats["uptime"],
        }

    def get_processed_events(self):
        return get_events()