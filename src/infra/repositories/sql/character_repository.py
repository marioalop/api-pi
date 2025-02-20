from typing import List

from domain.entities.schemas import CharacterPartialSchema, CharacterSchema
from domain.repositories.character_repository import (
    CharacterRepositoryInterface,
)
from infra.repositories.sql.base import DatabaseInitializer
from infra.repositories.sql.models import Character
from settings import DatabaseSettings


class CharacterRepository(CharacterRepositoryInterface):
    """
    A Concrete class to CRUD characters in a SQL database.
    """

    DATABASE_URL: str = DatabaseSettings.CONNECTION_STRING

    def __init__(self):
        """
        Constructor method.
        """
        self._db_initializer = DatabaseInitializer(self.DATABASE_URL)

    def get_characters(self) -> List[CharacterPartialSchema]:
        """
        Get all characters from the database.

        Returns:
            List[CharacterPartialSchema]: A list of characters.
        """
        session = self._db_initializer.get_session()
        try:
            characters = session.query(Character).all()
            return [
                CharacterPartialSchema.model_validate(character)
                for character in characters
            ]
        finally:
            session.close()

    def get_character(self, character_id: int) -> CharacterSchema | None:
        """
        Get a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            CharacterSchema | None: The character if found, None otherwise.
        """
        session = self._db_initializer.get_session()
        try:
            character = (
                session.query(Character)
                .filter(Character.id == character_id)
                .first()
            )
            if character:
                return CharacterSchema.model_validate(character)
            return None
        finally:
            session.close()

    def create_character(self, character: CharacterSchema) -> CharacterSchema:
        """
        Create a new character.

        Args:
            character (CharacterSchema): The character to create.

        Returns:
            CharacterSchema: The created character.
        """
        session = self._db_initializer.get_session()
        try:
            new_character = Character(**character.model_dump())
            session.add(new_character)
            session.commit()
            session.refresh(new_character)
            return CharacterSchema.model_validate(new_character)
        finally:
            session.close()

    def delete_character(self, character_id: int) -> bool:
        """
        Delete a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            bool: True if the character was deleted, False otherwise
        """
        session = self._db_initializer.get_session()
        try:
            character = (
                session.query(Character)
                .filter(Character.id == character_id)
                .first()
            )
            if character:
                session.delete(character)
                session.commit()
                return True
            return False
        finally:
            session.close()
