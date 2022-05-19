from django.urls import path

from crm.views import ClientViewset

urlpatterns = [
    path("clients/", ClientViewset.as_view({"get": "list", "post": "create"})),
    path(
        "clients/<int:pk>/",
        ClientViewset.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
