from django.urls import path

from contracts.views import ContractViewset

urlpatterns = [
    path("", ContractViewset.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        ContractViewset.as_view({"get": "retrieve", "put": "update"}),
    ),
]
