from django.urls import path
from . import views
from event.views import IndexView

app_name = "event"

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("eventlist/", views.eventlist, name="eventlist"),
    # path("<int:event_id>/detail/", views.detail, name="detail"),
    path("CreateEvent/", views.CreateEvent, name="CreateEvent"),
]
