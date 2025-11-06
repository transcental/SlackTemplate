from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from app.config import config

DB = PostgresEngine(config={"dsn": config.database_url.encoded_string()})

APP_REGISTRY = AppRegistry(apps=["app.piccolo_app"])
