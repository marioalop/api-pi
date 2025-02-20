import os

DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"
ENV = os.getenv("ENV", "dev")


class WebServerSettings:
    WEB_SERVER_HOST = os.getenv("WEB_SERVER_HOST")
    WEB_SERVER_PORT = os.getenv("WEB_SERVER_PORT")


class DatabaseSettings:
    DRIVER = os.getenv("DB_DRIVER", "sqlite")
    CONNECTION_STRING = os.getenv(
        "DB_CONNECTION_STRING"
    )

