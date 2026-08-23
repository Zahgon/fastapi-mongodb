import pytest

from greens.config import settings as global_settings
from greens.main import create_app
from greens.utils import get_logger, init_mongo


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    # Initialize MongoDB for testing
    with app.app_context():
        from flask import g
        g.logger = get_logger(__name__)
        g.mongo_client, g.mongo_db, g.mongo_collection = init_mongo(
            global_settings.mongodb_test,
            global_settings.mongodb_url.unicode_string(),
            global_settings.mongodb_collection,
        )
    
    yield app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner."""
    return app.test_cli_runner()
