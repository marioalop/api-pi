from domain.entities.schemas import CharacterSchema
from domain.repositories.character_repository import (
    CharacterRepositoryInterface,
)


class CharacterCreator:
    """
    A class to create a new character.
    """

    def __init__(self, character_repository: CharacterRepositoryInterface):
        """
        Constructor method.

        Args:
            character_repository (CharacterRepositoryInterface): An instance of
                a character repository.
        """
        self._character_repository = character_repository

    def create_character(self, character: CharacterSchema) -> CharacterSchema:
        """
        Create a new character.

        Args:
            character (CharacterSchema): The character to create.

        Returns:
            CharacterSchema: The created character.
        """
        return self._character_repository.create_character(character)
