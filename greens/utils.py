import logging
from functools import lru_cache

from pymongo import MongoClient
from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=150, style="blue")


@lru_cache
def get_logger(module_name):
    """
    Get a logger instance with Rich handler.

    Args:
        module_name: Name of the module requesting the logger.

    Returns:
        Logger instance configured with RichHandler.
    """
    logger = logging.getLogger(module_name)
    handler = RichHandler(rich_tracebacks=True, console=console, tracebacks_show_locals=True)
    handler.setFormatter(logging.Formatter("%(name)s - [ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def init_mongo(db_name: str, db_url: str, collection: str):
    """
    Initialize MongoDB connection (synchronous).

    Args:
        db_name: Database name.
        db_url: MongoDB connection URL.
        collection: Collection name.

    Returns:
        Tuple of (mongo_client, mongo_database, mongo_collections dict).
    """
    mongo_client = MongoClient(db_url)
    mongo_database = mongo_client[db_name]
    mongo_collections = {
        collection: mongo_database.get_collection(collection),
    }
    return mongo_client, mongo_database, mongo_collections
