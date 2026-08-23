import pytest
from bson import ObjectId

from greens.schemas.vegs import DocumentResponse


def create_valid_objectid():
    """Helper function to create a valid ObjectId instance."""
    return ObjectId()


def create_invalid_objectid():
    """Helper function to create an invalid ObjectId string."""
    return "invalid_objectid"


@pytest.mark.parametrize(
    "test_id, object_id",
    [
        ("HP-1", create_valid_objectid()),
    ],
)
def test_document_response_with_valid_id(test_id, object_id):
    """Test DocumentResponse accepts valid ObjectId."""
    document_response = DocumentResponse(id=object_id)
    assert document_response.id == str(object_id), \
        f"Test case {test_id} failed: The id field did not match the input ObjectId."


@pytest.mark.parametrize(
    "test_id, object_id, expected_exception",
    [
        ("EC-1", create_invalid_objectid(), ValueError),
        ("EC-2", None, ValueError),
        ("EC-3", 12345, ValueError),
    ],
)
def test_document_response_with_invalid_id(test_id, object_id, expected_exception):
    """Test DocumentResponse raises ValueError for invalid ObjectId."""
    with pytest.raises(expected_exception) as exc_info:
        DocumentResponse(id=object_id)
    assert str(exc_info.value), \
        f"Test case {test_id} failed: Expected exception {expected_exception} was not raised."
