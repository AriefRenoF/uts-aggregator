import pytest
from src.models import Event
from src.event_processor import EventProcessor

@pytest.fixture
def processor():
    return EventProcessor()

def test_publish_event(processor):
    event = Event(topic="test", event_id="1", timestamp="2023-10-01T00:00:00Z", source="test_source", payload={})
    await processor.publish([event])
    assert processor.stats["received"] == 1
    assert processor.stats["unique_processed"] == 1

def test_duplicate_event(processor):
    event = Event(topic="test", event_id="1", timestamp="2023-10-01T00:00:00Z", source="test_source", payload={})
    await processor.publish([event])
    await processor.publish([event])  # Duplicate
    assert processor.stats["duplicate_dropped"] == 1