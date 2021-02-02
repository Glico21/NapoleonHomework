def owner_required(method):
    async def check(self, *args, **kwargs):
        if self.auth_required:
            token = kwargs['token']
            uid = kwargs.get('uid')
            if token.get('uid') != uid:
                return await self.make_response_json(status=403)
        return await method(self, *args, **kwargs)
    return check
