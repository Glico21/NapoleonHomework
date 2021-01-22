from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HelloEndpoint(
            config=config, context=context, uri='/', methods=('GET', 'POST')
        ),
        endpoints.CreateUserEndpoint(
            config, context, uri='/user', methods=['POST']
        ),
        endpoints.AuthUserEndpoint(
            config, context, uri='user/auth', methods=['POST']
        ),
        endpoints.ModifyUserEndpoint(
            config, context, uri='/user/<uid:int>', methods=['PATCH', 'DELETE'], auth_required=True
        ),
        endpoints.AllUserEndpoint(
            config, context, uri='/user/all', methods=['GET'], auth_required=True,
        ),
        endpoints.OneUserEndpoint(
            config, context, uri='/user/<uid:int>', methods=['GET'], auth_required=True,
        )
    )
