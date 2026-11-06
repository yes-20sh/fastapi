import uuid


def test_health_ping(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_health(client):
    # 1. Create a health record
    payload = {"name": "server-node-1"}
    post_res = client.post("/api/v1/health", json=payload)
    assert post_res.status_code == 201
    created_data = post_res.json()
    assert created_data["name"] == "server-node-1"
    assert "id" in created_data
    assert "date_time" in created_data

    # Verify ID is a valid UUID
    record_uuid = uuid.UUID(created_data["id"])
    assert str(record_uuid) == created_data["id"]

    # 2. Get all health records
    get_res = client.get("/api/v1/health")
    assert get_res.status_code == 200
    all_records = get_res.json()
    assert isinstance(all_records, list)
    assert any(record["id"] == created_data["id"] for record in all_records)
