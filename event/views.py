from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect
from django.shortcuts import reverse
from django.views.generic import TemplateView

from .models import Event


class IndexView(TemplateView):
    template_name = "event/index.html"


def eventlist(request):
    latest_event_list = Event.objects.order_by("event_text")
    context = {"latest_event_list": latest_event_list}
    return render(request, "event/eventlist.html", context)


def CreateEvent(request):
    c = Event(event_text=request.POST["text"])
    if c.event_text != "":
        c.save()

    return HttpResponsePermanentRedirect(reverse("event:eventlist"))
