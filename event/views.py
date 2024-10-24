from django.views.generic import TemplateView
from .models import Event


class IndexView(TemplateView):
    template_name = "event/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by("-pub_date")[:5]
