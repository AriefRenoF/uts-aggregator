import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Event
from datetime import datetime

client = TestClient(app)

# Tes untuk endpoint POST /publish
def test_publish_single_event():
    event = {
        "topic": "test_topic",
        "event_id": "unique_event_id_1",
        "timestamp": datetime.now().isoformat(),
        "source": "test_source",
        "payload": {"key": "value"}
    }
    response = client.post("/publish", json=[event])
    assert response.status_code == 200
    assert response.json() == {"message": "Events processed"}

# Tes untuk endpoint GET /events
def test_get_events():
    response = client.get("/events?topic=test_topic")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Tes untuk endpoint GET /stats
def test_get_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    stats = response.json()
    assert "received" in stats
    assert "unique_processed" in stats
    assert "duplicate_dropped" in stats
    assert "topics" in stats
