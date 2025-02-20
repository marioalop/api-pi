from typing import List

from domain.entities.exceptions import CharacterNotFoundError
from domain.entities.schemas import CharacterSchema
from domain.repositories.character_repository import (
    CharacterRepositoryInterface,
)


class CharacterInspector:
    """
    A class to list characters.
    """

    def __init__(self, character_repository: CharacterRepositoryInterface):
        """
        Constructor method.

        Args:
            character_repository (CharacterRepositoryInterface): An instance of
                a character repository.
        """
        self._character_repository = character_repository

    def list_characters(self) -> List[CharacterSchema]:
        """
        List all characters.

        Returns:
            List[CharacterSchema]: A list of characters.
        """
        return self._character_repository.get_characters()

    def get_character(self, character_id: int) -> CharacterSchema:
        """
        Get a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            CharacterSchema: The character.

        Raises:
            CharacterNotFoundError: If the character is not found.
        """
        char = self._character_repository.get_character(character_id)
        if char is None:
            raise CharacterNotFoundError(character_id)
        return char
