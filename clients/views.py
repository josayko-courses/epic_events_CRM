from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import ClientPermission, isManagement
from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, isManagement | ClientPermission]

    def get_queryset(self):
        """
        Get all clients
        """
        return Client.objects.all()

    def perform_create(self, serializer):
        """
        Bind sales contact to request user
        """
        serializer.save(sales_contact=self.request.user)
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