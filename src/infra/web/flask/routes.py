from infra.web.flask.constants import INDEX_TEXT, Paths
from infra.web.flask.constants import ViewNames as names
from infra.web.flask.views.characters_views import (
    CharacterDetailDELETEView,
    CharacterDetailGETView,
    CharacterDetailPOSTView,
    CharacterListView,
)
from infra.web.flask.views.doc_views import OpenApiJsonView

ROUTES = {
    Paths.INDEX: lambda: INDEX_TEXT,
    Paths.CHAR_ALL: CharacterListView.as_view(names.CHAR_LIST),
    Paths.CHAR_ADD: CharacterDetailPOSTView.as_view(names.CHAR_GET),
    Paths.CHAR_GET: CharacterDetailGETView.as_view(names.CHAR_POST),
    Paths.CHAR_DEL: CharacterDetailDELETEView.as_view(names.CHAR_DEL),
    Paths.OPENAPI_JSON: OpenApiJsonView.as_view(names.OPENAPI_JSON),
}
