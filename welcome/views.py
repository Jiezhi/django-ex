import os
from django.shortcuts import render
from . import database
from django.conf import settings
from django.http import HttpResponse

from .models import PageView


# Create your views here.
def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })


def health(request):
    return HttpResponse(PageView.objects.count())
