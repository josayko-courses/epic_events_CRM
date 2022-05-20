from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import ContractPermission, isManagement
from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, isManagement | ContractPermission]

    def get_queryset(self):
        """
        Get all contracts
        """
        return Contract.objects.all()

    def perform_create(self, serializer):
        """
        Cannot create a contract with a prospect
        """
        if serializer.validated_data.get("client").is_customer is False:
            raise PermissionDenied("Cannot create a contract with a prospect")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        """
        Cannot update a signed contract
        """
        contract = self.get_object()
        if contract.is_signed is True:
            if serializer.validated_data.get("is_signed") is False:
                raise PermissionDenied("Cannot update a signed contract")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
