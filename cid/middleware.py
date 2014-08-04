from django.conf import settings

from .locals import set_cid, get_cid


class CidMiddleware(object):
    """
    Middleware class to extract the correlation id from incoming headers
    and add them to out going headers
    """

    def __init__(self):
        self.cid_header = getattr(settings, 'CID_HEADER', 'X_CORRELATION_ID')

    def process_request(self, request):
        set_cid(request.META.get(self.cid_header, None))

    def process_response(self, request, response):
        cid = get_cid()
        if cid:
            response[self.cid_header] = cid
