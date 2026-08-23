from inline_snapshot import snapshot


def test_health_check(client):
    """Test health check endpoint returns MongoDB metadata."""
    response = client.get("/health-check")
    assert response.status_code == 200
    data = response.get_json()
    assert "version" in data
    assert "databases" in data
    assert "collections" in data
