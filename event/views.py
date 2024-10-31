# from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Event


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "event/index.html", context)
