from django.shortcuts import render

from core.models import Monitor


def home(request):
    context = dict(monitors=Monitor.objects.filter())
    return render(request, 'core/monitors_overview.html', context)
