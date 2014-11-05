from uuid import uuid4
from django.conf import settings

from .locals import set_cid, get_cid


class CidMiddleware(object):
    """
    Middleware class to extract the correlation id from incoming headers
    and add them to out going headers
    """

    def __init__(self):
        self.cid_header = getattr(settings, 'CID_HEADER', 'X_CORRELATION_ID')
        self.generate_cid = getattr(settings, 'CID_GENERATE', False)

    def process_request(self, request):
        cid = request.META.get(self.cid_header, None)
        if cid is None and self.generate_cid:
            cid = str(uuid4())
        request.correlation_id = cid
        set_cid(request.correlation_id)

    def process_response(self, request, response):
        cid = get_cid()
        if cid:
            response[self.cid_header] = cid
        return response
