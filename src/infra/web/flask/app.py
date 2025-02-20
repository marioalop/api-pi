from typing import Callable, Dict

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

import settings
from infra.web.flask.constants import API_NAME, Paths
from infra.web.flask.routes import ROUTES


class CharacterCRUDApp(Flask):
    """
    The CharacterCRUDApp Flask App class
    """

    _url_map: Dict[str, Callable] = ROUTES

    def __init__(self, *args, **kwargs):
        """
        The constructor method
        """
        self._debug_mode = settings.DEBUG_MODE
        super().__init__(
            *args,
            **kwargs,
        )
        for url, view in self._url_map.items():
            self.add_url_rule(url, view_func=view)

        swaggerui_blueprint = get_swaggerui_blueprint(
            Paths.SWAGGER_UI,
            Paths.OPENAPI_JSON,
            config=dict(app_name=API_NAME),
        )
        self.register_blueprint(
            swaggerui_blueprint, url_prefix=Paths.SWAGGER_UI
        )

    def run(self, *args, **kwargs):
        """
        Start the Flask app
        """
        super().run(
            *args,
            host=settings.WebServerSettings.WEB_SERVER_HOST,
            port=settings.WebServerSettings.WEB_SERVER_PORT,
            debug=self._debug_mode,
            **kwargs,
        )
