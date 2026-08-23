from flask import jsonify
from werkzeug.exceptions import HTTPException


class NotFoundException(HTTPException):
    """Exception for 404 Not Found responses."""
    code = 404
    
    def __init__(self, msg: str = None):
        super().__init__(description=msg if msg else "Requested resource is not found")
        self.msg = msg
    
    def get_response(self, environ=None):
        response = jsonify({"detail": self.description})
        response.status_code = self.code
        return response


class AlreadyExistsException(HTTPException):
    """Exception for 409 Conflict responses."""
    code = 409
    
    def __init__(self, msg: str = None):
        super().__init__(description=msg if msg else "Document with specified id already exists")
        self.msg = msg
    
    def get_response(self, environ=None):
        response = jsonify({"detail": self.description})
        response.status_code = self.code
        return response
