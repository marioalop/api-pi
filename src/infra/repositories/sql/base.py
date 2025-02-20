import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()


class DatabaseInitializer:
    """
    Handles database initialization logic such as file creation (for SQLite) and table setup.
    """

    def __init__(self, database_url: str):
        """
        Constructor method.

        Args:
            database_url (str): The URL of the database
        """
        self._database_url = database_url
        self._engine = None
        self._SessionLocal = None
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the database engine, create files if needed
            (SQLite), and create tables.
        """
        if self._database_url.startswith("sqlite"):
            db_path = self._database_url.replace("sqlite:///", "")
            if not os.path.exists(db_path):
                os.makedirs(os.path.dirname(db_path), exist_ok=True)
                open(db_path, "a").close()

        self._engine = create_engine(self._database_url, echo=True)
        Base.metadata.create_all(self._engine)
        self._SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine
        )

    def get_session(self) -> Session:
        """
        Provides a new SQLAlchemy session.

        Returns:
            Session: A new session object.
        """
        return self._SessionLocal()
