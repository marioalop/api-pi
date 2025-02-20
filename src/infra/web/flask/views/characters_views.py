from flask import Response, jsonify, request
from flask.views import MethodView

from application.character_creator import CharacterCreator
from application.character_inspector import CharacterInspector
from application.character_remover import CharacterRemover
from domain.entities.schemas import CharacterSchema
from infra.repositories.sql.character_repository import CharacterRepository
from infra.web.flask.enums import HttpStatusCodes
from infra.web.flask.schemas import ResponseMessageSchema


class CharacterListView(MethodView):
    """
    The CharacterListView class.
    """

    def get(self) -> Response:
        """
        Get all characters.

        Returns:
            Response: The response.
        """
        character_inspector = CharacterInspector(CharacterRepository())
        try:
            characters = character_inspector.list_characters()
        except Exception as e:
            return (
                jsonify(ResponseMessageSchema(message=str(e)).model_dump()),
                HttpStatusCodes.BAD_REQUEST.value,
            )
        return jsonify([c.model_dump() for c in characters])


class CharacterDetailGETView(MethodView):
    """
    The CharacterDetailView class GET method.
    """

    def get(self, character_id: int) -> Response:
        """
        Get a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            Response: The response.
        """
        character_inspector = CharacterInspector(CharacterRepository())
        try:
            character = character_inspector.get_character(character_id)
        except Exception as e:
            return (
                jsonify(ResponseMessageSchema(message=str(e)).model_dump()),
                HttpStatusCodes.BAD_REQUEST.value,
            )
        return jsonify(character.model_dump())


class CharacterDetailPOSTView(MethodView):
    """
    The CharacterDetailView class POST method.
    """

    def post(self) -> Response:
        """
        Create a new character.

        Returns:
            Response: The response.
        """
        character_creator = CharacterCreator(CharacterRepository())
        try:
            input_data = CharacterSchema.model_validate(request.json)
        except Exception as e:
            return (
                jsonify(ResponseMessageSchema(message=str(e)).model_dump()),
                HttpStatusCodes.BAD_REQUEST.value,
            )
        try:
            character = character_creator.create_character(input_data)
        except Exception as e:
            return (
                jsonify(ResponseMessageSchema(message=str(
                    f"Character ID: {input_data.id} already exists"
                    )).model_dump()),
                HttpStatusCodes.BAD_REQUEST.value,
            )
        return jsonify(character.model_dump()), HttpStatusCodes.CREATED.value


class CharacterDetailDELETEView(MethodView):
    """
    The CharacterDetailView class DELETE method.
    """

    def delete(self, character_id: int) -> Response:
        """
        Delete a character by its ID.

        Args:
            character_id (int): The ID of the character.

        Returns:
            Response: The response.
        """
        character_remover = CharacterRemover(CharacterRepository())
        removed = character_remover.remove_character(character_id)
        if removed:
            return jsonify(
                ResponseMessageSchema(message="Character removed").model_dump()
            )
        return (
            jsonify(
                ResponseMessageSchema(
                    message="Character not found"
                ).model_dump()
            ),
            HttpStatusCodes.BAD_REQUEST.value,
        )
