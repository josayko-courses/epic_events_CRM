from django.urls import path

from events.views import EventViewset

urlpatterns = [
    path("", EventViewset.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        EventViewset.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
