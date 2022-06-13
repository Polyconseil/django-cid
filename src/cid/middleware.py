from django.conf import settings

from cid.locals import generate_new_cid
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
        upstream_cid = request.META.get(self.cid_request_header, None)
        cid = generate_new_cid(upstream_cid)
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
