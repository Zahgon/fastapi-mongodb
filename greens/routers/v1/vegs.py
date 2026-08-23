from flask import Blueprint, request, jsonify

from greens.config import settings as global_settings
from greens.routers.exceptions import NotFoundException
from greens.schemas.vegs import Document, DocumentResponse
from greens.services.repository import create_document, retrieve_document

collection = global_settings.mongodb_collection

bp = Blueprint('vegs', __name__)


@bp.route("", methods=["POST"])
def add_document():
    """
    Create a new document.

    Returns:
        JSON response with created document ID.
    """
    try:
        payload_data = request.get_json()
        payload = Document(**payload_data)
        document = create_document(payload, collection)
        response = DocumentResponse(id=document.inserted_id)
        return jsonify(response.model_dump()), 201
    except ValueError as exception:
        raise NotFoundException(msg=str(exception)) from exception


@bp.route("/<object_id>", methods=["GET"])
def get_document(object_id: str):
    """
    Retrieve a document by ID.

    Args:
        object_id: MongoDB ObjectId as string.

    Returns:
        JSON response with document data.
    """
    try:
        document = retrieve_document(object_id, collection)
        response = DocumentResponse(id=document["id"])
        return jsonify(response.model_dump())
    except (ValueError, TypeError) as exception:
        raise NotFoundException(msg=str(exception)) from exception
