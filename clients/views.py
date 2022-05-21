from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from authentication.permissions import ClientPermission, isManagement
from clients.models import Client
from clients.serializers import ClientSerializer
from events.models import Event


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, isManagement | ClientPermission]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    # /clients/?is_customer=true
    filterset_fields = ["is_customer"]
    # /clients/?search=Microsoft
    search_fields = ["^company_name", "^last_name", "^email"]

    def get_queryset(self):
        """
        Management can read all clients.
          SALES:    - Can read all prospects and/or their own customers
        SUPPORT:    - Can read their own customers
        """
        if self.request.user.role == "SALES":
            prospects = Client.objects.filter(is_customer=False)
            customers = Client.objects.filter(sales_contact=self.request.user.id)
            return prospects | customers
        elif self.request.user.role == "SUPPORT":
            events = Event.objects.filter(support_contact=self.request.user)
            return [e.contract.client for e in events]
        return Client.objects.all()

    def perform_create(self, serializer):
        """
        Bind sales contact to request user
        """
        if serializer.validated_data.get("is_customer") is True:
            serializer.save(sales_contact=self.request.user)
        else:
            serializer.save(sales_contact=None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        """
        Cannot update a customer back to propspect
        """
        client = self.get_object()
        if client.is_customer is True:
            if serializer.validated_data.get("is_customer") is False:
                raise PermissionDenied("Cannot update a customer back to prospect")
        serializer.save(sales_contact=self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
