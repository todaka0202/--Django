# from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Event


# class IndexView(TemplateView):
#     template_name = "event/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Event.objects.order_by("-pub_date")[:5]


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "event/index.html", context)


# def vote(request, event_id)
