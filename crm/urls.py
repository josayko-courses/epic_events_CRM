from crm.views import ClientViewset
from django.urls import path

urlpatterns = [
    path("clients/", ClientViewset.as_view({"get": "list"})),
]
