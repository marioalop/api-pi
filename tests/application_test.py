from unittest.mock import MagicMock

import pytest
from faker import Faker

from application.character_creator import CharacterCreator
from application.character_inspector import CharacterInspector
from application.character_remover import CharacterRemover
from domain.entities.exceptions import CharacterNotFoundError
from domain.entities.schemas import CharacterSchema

fake = Faker()


@pytest.fixture
def mock_repository():
    return MagicMock()


@pytest.fixture
def character_data():
    return CharacterSchema(
        id=None,
        name=fake.first_name(),
        height=fake.random_number(digits=3),
        mass=fake.random_number(digits=2),
        hair_color=fake.color_name(),
        skin_color=fake.color_name(),
        eye_color=fake.color_name(),
        birth_year=fake.random_number(digits=2),
    )



def test_create_character(mock_repository, character_data):
    creator = CharacterCreator(mock_repository)
    mock_repository.create_character.return_value = character_data

    result = creator.create_character(character_data)

    mock_repository.create_character.assert_called_once_with(character_data)
    assert result == character_data



def test_list_characters(mock_repository, character_data):
    inspector = CharacterInspector(mock_repository)
    mock_repository.get_characters.return_value = [character_data]

    result = inspector.list_characters()

    mock_repository.get_characters.assert_called_once()
    assert len(result) == 1
    assert result[0] == character_data


def test_get_character_found(mock_repository, character_data):
    inspector = CharacterInspector(mock_repository)
    mock_repository.get_character.return_value = character_data

    result = inspector.get_character(1)

    mock_repository.get_character.assert_called_once_with(1)
    assert result == character_data


def test_get_character_not_found(mock_repository):
    inspector = CharacterInspector(mock_repository)
    mock_repository.get_character.return_value = None

    with pytest.raises(CharacterNotFoundError) as exc_info:
        inspector.get_character(999)

    mock_repository.get_character.assert_called_once_with(999)
    assert str(exc_info.value) == "Character with ID 999 not found"



def test_remove_character_success(mock_repository):
    remover = CharacterRemover(mock_repository)
    mock_repository.delete_character.return_value = True

    result = remover.remove_character(1)

    mock_repository.delete_character.assert_called_once_with(1)
    assert result is True


def test_remove_character_not_found(mock_repository):
    remover = CharacterRemover(mock_repository)
    mock_repository.delete_character.return_value = False

    result = remover.remove_character(999)

    mock_repository.delete_character.assert_called_once_with(999)
    assert result is False
