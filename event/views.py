from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic

from .models import Event
from .models import DateChoice

# from .models import DateChoice


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


class DetailView(generic.DetailView):
    template_name = "event/event_detail.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({"event_date_list": DateChoice.objects.order_by("event_date")})
        return context


def CreateEvent(request):
    c = Event(event_text=request.POST["text"])
    # e = DateChoice(event_date=request.POST["date"])

    if c.event_text != "":
        c.save()

    # if e.event_date != "":
    #     e.save()

    return HttpResponsePermanentRedirect(reverse("event:eventlist"))


def DeleteEvent(request, event_id):
    target_event = Event.objects.get(id=event_id)
    target_event.delete()
    return HttpResponsePermanentRedirect(reverse("event:eventlist"))


def edit(request, event_id):
    target_event = Event.objects.get(id=event_id)
    context = {"event": target_event}
    return render(request, "event/edit.html", context)


def update(request, event_id):
    target_event = Event.objects.get(id=event_id)

    target_event.event_text = request.POST.get('title')
    target_event.save()
    return HttpResponseRedirect(reverse("event:eventlist"))
