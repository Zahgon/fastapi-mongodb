import pytest
from bson import ObjectId


@pytest.mark.parametrize(
    "payload, status_code",
    [
        (
            {"name": "Corn", "desc": "Corn on the cob"},
            201,
        ),
    ],
)
def test_add_document(client, payload: dict, status_code: int):
    """Test document creation endpoint."""
    response = client.post("/api/v1/vegs", json=payload)
    assert response.status_code == status_code
    data = response.get_json()
    assert ObjectId.is_valid(data["id"])
