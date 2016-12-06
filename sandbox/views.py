from django.http import HttpResponse


def ping_view(request, *args, **kwargs):
    return HttpResponse('OK')
