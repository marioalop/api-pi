from typing import Any, Dict, List, Optional, Type

from pydantic import BaseModel, TypeAdapter


class OpenAPIBuilder:
    """
    Builder class for generating OpenAPI JSON documentation.
    """

    def __init__(self, title: str, version: str, description: str = ""):
        self._openapi_doc: Dict[str, Any] = {
            "openapi": "3.0.0",
            "info": {
                "title": title,
                "version": version,
                "description": description,
            },
            "paths": {},
            "components": {"schemas": {}},
        }

    def add_endpoint(
        self,
        path: str,
        input_model: Optional[Type[BaseModel]],
        response_model_ok: Type[BaseModel] | TypeAdapter[List[BaseModel]],
        status_code_ok: int,
        response_model_bad: Type[BaseModel],
        status_code_bad: int,
        method: str,
        path_parameters: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Add an endpoint to the OpenAPI JSON documentation.

        Args:
            path (str): The path of the endpoint.
            input_model (Type[BaseModel] | None): The input model for the endpoint.
            response_model_ok (Type[BaseModel] | TypeAdapter[List[BaseModel]]): The response model for success.
            status_code_ok (int): The status code for a successful response.
            response_model_bad (Type[BaseModel]): The response model for an error response.
            status_code_bad (int): The status code for an error response.
            method (str): The HTTP method of the endpoint.
            path_parameters (List[Dict[str, Any]], optional): Path parameters metadata.
        """
        method = method.lower()
        if path not in self._openapi_doc["paths"]:
            self._openapi_doc["paths"][path] = {}

        endpoint_doc = {
            "responses": {
                str(status_code_ok): {
                    "description": "Successful response",
                    "content": {
                        "application/json": {
                            "schema": self._model_to_schema(response_model_ok)
                        }
                    },
                },
                str(status_code_bad): {
                    "description": "Error response",
                    "content": {
                        "application/json": {
                            "schema": self._model_to_schema(response_model_bad)
                        }
                    },
                },
            }
        }

        if input_model:
            endpoint_doc["requestBody"] = {
                "content": {
                    "application/json": {
                        "schema": self._model_to_schema(input_model)
                    }
                }
            }

        if path_parameters:
            endpoint_doc["parameters"] = []
            for param in path_parameters:
                endpoint_doc["parameters"].append(
                    {
                        "name": param["name"],
                        "in": "path",
                        "required": True,
                        "description": param.get("description", ""),
                        "schema": {"type": param.get("type", "string")},
                    }
                )

        self._openapi_doc["paths"][path][method] = endpoint_doc

    def build(self) -> Dict[str, Any]:
        """
        Build and return the OpenAPI JSON documentation.

        Returns:
            Dict[str, Any]: The OpenAPI JSON documentation.
        """
        return self._openapi_doc

    def _model_to_schema(
        self, model: Type[BaseModel] | TypeAdapter[List[BaseModel]]
    ) -> Dict[str, Any]:
        """
        Convert a Pydantic model to an OpenAPI-compatible schema.

        Args:
            model (Type[BaseModel] | TypeAdapter[List[BaseModel]]):
                The Pydantic model to convert.

        Returns:
            Dict[str, Any]: The OpenAPI-compatible schema.
        """
        if isinstance(model, TypeAdapter):
            model_name = model.core_schema["items_schema"]["cls"].__name__
            if model_name not in self._openapi_doc["components"]["schemas"]:
                schema = model.core_schema["items_schema"][
                    "cls"
                ].model_json_schema(
                    ref_template="#/components/schemas/{model}"
                )
                self._openapi_doc["components"]["schemas"][model_name] = schema
            return {
                "type": "array",
                "items": {"$ref": f"#/components/schemas/{model_name}"},
            }
        else:
            return self._add_model_schema(model)

    def _add_model_schema(self, model: Type[BaseModel]) -> Dict[str, Any]:
        """
        Add a Pydantic model schema to the OpenAPI components.

        Args:
            model (Type[BaseModel]): The Pydantic model to add.

        Returns:
            Dict[str, Any]: The OpenAPI-compatible schema
        """
        model_name = model.__name__
        if model_name not in self._openapi_doc["components"]["schemas"]:
            schema = model.model_json_schema(
                ref_template="#/components/schemas/{model}"
            )
            self._openapi_doc["components"]["schemas"][model_name] = schema
        return {"$ref": f"#/components/schemas/{model_name}"}
