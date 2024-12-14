from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("EventList/", views.EventListView.as_view(), name="eventlist"),
    # path("<int:event_id>/detail/", views.detail, name="detail"),
    path("CreateEvent/", views.CreateEvent, name="CreateEvent"),
]
