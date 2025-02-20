from typing import List

from flask import Response, jsonify, request
from flask.views import MethodView
from pydantic import TypeAdapter

from domain.entities.schemas import CharacterPartialSchema, CharacterSchema
from infra.web.flask import constants as cts
from infra.web.flask.enums import HttpMethods, HttpStatusCodes
from infra.web.flask.openapi_builder import OpenAPIBuilder
from infra.web.flask.schemas import ResponseMessageSchema


class OpenApiJsonView(MethodView):
    """
    The OpenApiJsonView class.
    """

    def get(self) -> Response:
        """
        Get the OpenAPI JSON.

        Returns:
            Response: The response.
        """
        openapi_builder = OpenAPIBuilder(
            title=cts.API_NAME, version=cts.API_VERSION
        )
        openapi_builder.add_endpoint(
            path=cts.Paths.CHAR_ALL,
            input_model=None,
            response_model_ok=TypeAdapter(List[CharacterPartialSchema]),
            status_code_ok=HttpStatusCodes.OK.value,
            response_model_bad=ResponseMessageSchema,
            status_code_bad=HttpStatusCodes.BAD_REQUEST.value,
            method=HttpMethods.GET.value,
        )

        openapi_builder.add_endpoint(
            path=cts.Paths.CHAR_ADD,
            input_model=CharacterSchema,
            response_model_ok=CharacterSchema,
            status_code_ok=HttpStatusCodes.CREATED.value,
            response_model_bad=ResponseMessageSchema,
            status_code_bad=HttpStatusCodes.BAD_REQUEST.value,
            method=HttpMethods.POST.value,
        )

        openapi_builder.add_endpoint(
            path=cts.Paths.CHAR_GET_DOC,
            input_model=None,
            response_model_ok=CharacterSchema,
            status_code_ok=HttpStatusCodes.OK.value,
            response_model_bad=ResponseMessageSchema,
            status_code_bad=HttpStatusCodes.BAD_REQUEST.value,
            method=HttpMethods.GET.value,
            path_parameters=[
                {
                    "name": "character_id",
                    "type": "integer",
                    "description": "Character ID",
                }
            ],
        )

        openapi_builder.add_endpoint(
            path=cts.Paths.CHAR_DEL_DOC,
            input_model=None,
            response_model_ok=ResponseMessageSchema,
            status_code_ok=HttpStatusCodes.OK.value,
            response_model_bad=ResponseMessageSchema,
            status_code_bad=HttpStatusCodes.BAD_REQUEST.value,
            method=HttpMethods.DELETE.value,
            path_parameters=[
                {
                    "name": "character_id",
                    "type": "integer",
                    "description": "Character ID",
                }
            ],
        )

        return jsonify(openapi_builder.build())
