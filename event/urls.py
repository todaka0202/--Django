from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("eventlist/", views.eventlist, name="eventlist"),
    path("<int:event_id>/detail/", views.detail, name="detail"),
    path("CreateEvent/", views.CreateEvent, name="CreateEvent"),
]
