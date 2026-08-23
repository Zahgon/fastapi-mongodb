from flask import Blueprint

from greens.routers.v1.vegs import bp as vegs_bp

bp = Blueprint('v1', __name__)
bp.register_blueprint(vegs_bp, url_prefix="/vegs")
