from sanic import Sanic

from configs.config import AppConfig
from transport.sanic.routes import get_routes


def configure_app(config: AppConfig):

    app = Sanic(__name__)

    for handler in get_routes(config):
        app.add_route(
            handler=handler,
            uri=handler.uri,
            methods=handler.methods,
            strict_slashes=True,
        )

    return app
