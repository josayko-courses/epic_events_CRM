from django.urls import path

from crm.views import ClientViewset

urlpatterns = [
    path("clients/", ClientViewset.as_view({"get": "list"})),
]
