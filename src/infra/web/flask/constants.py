INDEX_TEXT: str = "Character API"
API_NAME: str = "Character CRUD API"
API_VERSION: str = "v1"


class Paths:
    INDEX: str = "/"
    CHAR_ALL: str = "/character/getAll"
    CHAR_ADD: str = "/character/add"
    CHAR_GET: str = "/character/get/<int:character_id>"
    CHAR_DEL: str = "/character/delete/<int:character_id>"
    OPENAPI_JSON: str = "/swagger.json"
    SWAGGER_UI: str = "/docs"
    CHAR_GET_DOC: str = "/character/get/{character_id}"
    CHAR_DEL_DOC: str = "/character/delete/{character_id}"


class ViewNames:
    CHAR_LIST: str = "character-list"
    CHAR_POST: str = "character-detail-post"
    CHAR_GET: str = "character-detail-get"
    CHAR_DEL: str = "character-detail-delete"
    OPENAPI_JSON: str = "openapi-json"
