from abc import ABC, abstractmethod
from typing import List

from domain.entities.schemas import CharacterPartialSchema, CharacterSchema


class CharacterRepositoryInterface(ABC):
    @abstractmethod
    def get_characters(self) -> List[CharacterPartialSchema]:
        """
        Get all characters from the database.

        Returns:
            List[CharacterSchema]: A list of characters.
        """

    @abstractmethod
    def get_character(self, character_id: int) -> CharacterSchema | None:
        """
        Get a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            CharacterSchema | None: The character if found, None otherwise.
        """

    @abstractmethod
    def create_character(self, character: CharacterSchema) -> CharacterSchema:
        """
        Create a new character.

        Args:
            character (CharacterSchema): The character to create.

        Returns:
            CharacterSchema: The created character.
        """

    @abstractmethod
    def delete_character(self, character_id: int) -> bool:
        """
        Delete a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            bool: True if the character was deleted, False otherwise
        """
