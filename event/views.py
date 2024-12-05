from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect
from django.shortcuts import reverse
from .models import Event


def index(request):
    return render(request, "event/index.html")


def detail(reqest, event_id):
    event = Event.objects.order_by("event_text")
    context = {"event": event}
    return render(reqest, "event/detail.html", context, event_id)


def eventlist(request):
    latest_event_list = Event.objects.order_by("event_text")
    context = {"latest_event_list": latest_event_list}
    return render(request, "event/eventlist.html", context)


def CreateEvent(request):
    c = Event(event_text=request.POST["text"])
    if c.event_text != "":
        c.save()

    return HttpResponsePermanentRedirect(reverse("event:eventlist"))
