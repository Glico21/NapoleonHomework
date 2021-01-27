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
            config, context, uri='/user/auth', methods=['POST']
        ),
        endpoints.ModifyUserEndpoint(
            config, context, uri='/user/<uid:int>', methods=['PATCH', 'DELETE'], auth_required=True
        ),
        endpoints.AllUserEndpoint(
            config, context, uri='/user/all', methods=['GET']
        ),
        endpoints.OneUserEndpoint(
            config, context, uri='/user/<uid:int>', methods=['GET'], auth_required=True
        ),
        endpoints.CreateMessageEndpoint(
            config, context, uri='/msg', methods=['POST'], auth_required=True
        ),
        endpoints.GetMessagesEndpoint(
            config, context, uri='/msg', methods=['GET'], auth_required=True
        ),
        endpoints.ModifyMessageEndpoint(
            config, context, uri='/msg/<message_id>', methods=['PATCH', 'DELETE'], auth_required=True
        ),
        endpoints.OneMessageEndpoint(
            config, context, uri='/msg/<message_id>', methods=['GET'], auth_required=True
        )
    )
