from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints
from transport.sanic.base import SanicEndpoint


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HelloEndpoint(config=config, context=context, uri='/', methods=('GET', 'POST')),
        endpoints.CreateUserEndpoint(config, context, uri='/user', methods=['POST']),
    )
