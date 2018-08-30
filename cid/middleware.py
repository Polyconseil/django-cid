from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from .locals import set_cid, get_cid


class CidMiddleware(MiddlewareMixin):
    """
    Middleware class to extract the correlation id from incoming headers
    and add them to outgoing headers
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cid_request_header = getattr(
            settings, 'CID_HEADER', 'X_CORRELATION_ID'
        )
        self.cid_response_header = getattr(
            settings, 'CID_RESPONSE_HEADER', self.cid_request_header
        )

    def process_request(self, request):
        cid = request.META.get(self.cid_request_header, None)
        if cid is None:
            cid = get_cid()
        request.correlation_id = cid
        set_cid(cid)

    def process_response(self, request, response):
        cid = get_cid()
        if cid and self.cid_response_header:
            response[self.cid_response_header] = cid
        return response
