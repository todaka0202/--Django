from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("eventlist/", views.EventListView.as_view(), name="eventlist"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("CreateEvent/", views.CreateEvent, name="CreateEvent"),
    path("delete/<int:event_id>", views.DeleteEvent, name="delete"),
    path("edit/<int:event_id>", views.edit, name="edit"),
    path("edit/<int:event_id>/update", views.update, name="update"),
]
