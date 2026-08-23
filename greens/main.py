from flask import Flask, g, jsonify

from greens.config import settings as global_settings
from greens.routers import bp as v1_bp
from greens.services.repository import get_mongo_meta
from greens.utils import get_logger, init_mongo


def create_app():
    """Application factory for Flask app."""
    app = Flask(__name__)
    
    if global_settings.environment == "local":
        get_logger("flask")
    
    @app.before_request
    def before_request():
        """Initialize MongoDB connection before each request if not exists."""
        if not hasattr(g, 'mongo_client'):
            g.logger = get_logger(__name__)
            g.mongo_client, g.mongo_db, g.mongo_collection = init_mongo(
                global_settings.mongodb_database,
                global_settings.mongodb_url.unicode_string(),
                global_settings.mongodb_collection,
            )
    
    @app.teardown_appcontext
    def teardown_db(exception):
        """Close MongoDB connection at end of request."""
        mongo_client = g.pop('mongo_client', None)
        if mongo_client is not None:
            mongo_client.close()
    
    # Register blueprints
    app.register_blueprint(v1_bp, url_prefix="/api/v1")
    
    @app.route("/health-check")
    def health_check():
        return jsonify(get_mongo_meta())
    
    return app


# Create app instance for direct running
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
