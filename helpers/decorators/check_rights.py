def check_id_rights_access_decorator(method):
    async def check_id_rights_access(self, request, body, *args, **kwargs):
        if self.auth_required:
            token = kwargs['token']
            uid = kwargs.get('uid')
            if token.get('uid') != uid:
                return await self.make_response_json(status=403)
        return await method(self, request, body, *args, **kwargs)
    return check_id_rights_access
