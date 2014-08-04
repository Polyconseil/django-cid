from django.conf import settings

from .locals import set_cid, get_cid


CID_HEADER = getattr(settings, 'CID_HEADER', 'X_CORRELATION_ID')


class CidMiddleware(object):

    def process_request(self, request):
        set_cid(request.META.get(CID_HEADER, None))

    def process_response(self, request, response):
        response[CID_HEADER] = get_cid()
