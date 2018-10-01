import logging

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from testapp.models import Item


logger = logging.getLogger('testapp')


def testit(request):
    logger.warning("This is a warning from django-cid test application.")
    list(Item.objects.all())
    context = {
        'sql_query': connection.queries[0]['sql'],
    }
    return render(request, 'testapp/testit.html', context)


def ok(request):
    """A simple view for integration tests."""
    return HttpResponse('ok')
