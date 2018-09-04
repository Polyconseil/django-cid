from django.conf import settings

from cid.locals import get_cid
from cid.locals import set_cid


class CidMiddleware:
    """
    Middleware class to extract the correlation id from incoming headers
    and add them to outgoing headers
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.cid_request_header = getattr(
            settings, 'CID_HEADER', 'X_CORRELATION_ID'
        )
        self.cid_response_header = getattr(
            settings, 'CID_RESPONSE_HEADER', self.cid_request_header
        )

    def _process_request(self, request):
        cid = request.META.get(self.cid_request_header, None)
        if cid is None:
            cid = get_cid()
        request.correlation_id = cid
        set_cid(cid)
        return request

    def _process_response(self, response):
        cid = get_cid()
        if cid and self.cid_response_header:
            response[self.cid_response_header] = cid
        return response

    def __call__(self, request):
        request = self._process_request(request)
        response = self.get_response(request)
        return self._process_response(response)


# FIXME: to be removed once we remove support of Django 1.11
class CidOldStyleMiddleware(CidMiddleware):
    """Support for the old ``MIDDLEWARE_CLASSES`` setting."""

    def __init__(self):
        print('middleware init')
        # `get_response` is only used in `CidMiddleware.__call__`,
        # which is not called when using `MIDDLEWARE_CLASSES`.
        super().__init__(get_response='dummy')

    def process_request(self, request):
        self._process_request(request)
        # We must return None otherwise Django thinks it's the
        # response.
        return None

    def process_response(self, request, response):
        return self._process_response(response)
