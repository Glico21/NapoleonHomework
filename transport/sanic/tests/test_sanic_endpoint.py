import pytest

from transport.sanic.base import SanicEndpoint


@pytest.mark.asyncio
async def test_valid_method_called(request_factory):
    methods = ['get', 'post', 'patch', 'delete']
    for method in methods:
        request = request_factory(method=method)

        endpoint = SanicEndpoint(None, None, '', ())

        response = await endpoint(request)
        assert response.body.decode() == f'{{"message":"Method {method.upper()} not implemented","error_code":500}}'
