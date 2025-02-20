from domain.entities.schemas import CharacterSchema
from domain.repositories.character_repository import (
    CharacterRepositoryInterface,
)


class CharacterRemover:
    """
    A class to remove a character.
    """

    def __init__(self, character_repository: CharacterRepositoryInterface):
        """
        Constructor method.

        Args:
            character_repository (CharacterRepositoryInterface): An instance of
                a character repository.
        """
        self._character_repository = character_repository

    def remove_character(self, character_id: int) -> bool:
        """
        Remove a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            bool: True if the character was removed, False otherwise.
        """
        return self._character_repository.delete_character(character_id)
