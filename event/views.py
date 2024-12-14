from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect
from django.shortcuts import reverse
from django.views import generic

from .models import Event
from .models import Date


class IndexView(generic.TemplateView):
    template_name = "event/index.html"


class EventListView(generic.ListView):
    template_name = "event/eventlist.html"
    context_object_name = "latest_event_list"
    model = Event

    def eventlist(self):
        latest_event_list = Event.objects.order_by("event_text")
        context = {"latest_event_list": latest_event_list}
        return render("event/eventlist.html", context)


def CreateEvent(request):
    c = Event(event_text=request.POST["text"])
    e = Date(event_date=request.POST["date"])

    if c.event_text != "":
        c.save()
    elif e.event_date != "":
        e.save()

    return HttpResponsePermanentRedirect(reverse("event:eventlist"))
