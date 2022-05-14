from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from crm.models import Client
from crm.serializers import ClientListSerializer


class ClientViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()

    def list(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
