from bson import ObjectId
from flask import g
from pymongo.errors import WriteError
from pymongo.results import InsertOneResult

from greens.routers.exceptions import AlreadyExistsException


def document_id_helper(document: dict) -> dict:
    """Convert MongoDB _id to id field."""
    document["id"] = document.pop("_id")
    return document


def retrieve_document(document_id: str, collection: str) -> dict:
    """
    Retrieve a document from MongoDB by ID.

    Args:
        document_id: The document's ObjectId as string.
        collection: Collection name.

    Returns:
        Document dict with id field.

    Raises:
        ValueError: If document not found.
    """
    document_filter = {"_id": ObjectId(document_id)}
    document = g.mongo_collection[collection].find_one(document_filter)
    if document:
        return document_id_helper(document)
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")


def create_document(document, collection: str) -> InsertOneResult:
    """
    Create a new document in MongoDB.

    Args:
        document: Pydantic model to insert.
        collection: Collection name.

    Returns:
        InsertOneResult from MongoDB.

    Raises:
        AlreadyExistsException: On write error.
    """
    try:
        result: InsertOneResult = g.mongo_collection[collection].insert_one(
            document.model_dump()
        )
        return result
    except WriteError as e:
        raise AlreadyExistsException(msg=str(e)) from e


def get_mongo_meta() -> dict:
    """
    Get MongoDB server metadata.

    Returns:
        Dict with version, databases, and collections info.
    """
    list_databases = g.mongo_client.list_database_names()
    list_of_collections = {}
    for db in list_databases:
        list_of_collections[db] = g.mongo_client[db].list_collection_names()
    mongo_meta = g.mongo_client.server_info()
    return {
        "version": mongo_meta["version"],
        "databases": list_databases,
        "collections": list_of_collections,
    }
