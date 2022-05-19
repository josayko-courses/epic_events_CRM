from django.urls import path

from crm.views import ClientViewset

urlpatterns = [
    path("", ClientViewset.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        ClientViewset.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
