from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission

from events.models import Event, EventStatus


class isManagement(BasePermission):
    """
    Read-only access through API endpoints, but can access Django
    admin dashboard for data modifications
    """

    def has_permission(self, request, view):
        return request.user.role == "MANAGEMENT" and request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class ClientPermission(BasePermission):
    """
      SALES:    - Create new clients
                - Read their own clients and any prospect
                - Update their own clients
                - Delete prospects only

    SUPPORT:    - Read their own clients
    """

    def has_permission(self, request, view):
        if request.user.role == "SUPPORT":
            return request.method in SAFE_METHODS
        return request.user.role == "SALES"

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return request.user.role == "SALES" and obj.is_customer is False
        elif request.user.role == "SUPPORT" and request.method in SAFE_METHODS:
            events = Event.objects.filter(support_contact=request.user)
            clients = [e.contract.client for e in events]
            return obj in clients
        return request.user == obj.sales_contact or obj.is_customer is False


class ContractPermission(BasePermission):
    """
      SALES:    - Create new contracts
                - Read their own contracts if not signed
                - Update their own contracts if not signed

    SUPPORT:    - Read their own clients contracts
    """

    def has_permission(self, request, view):
        if request.user.role == "SUPPORT":
            return request.method in SAFE_METHODS
        return request.user.role == "SALES"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.role == "SUPPORT":
                event = Event.objects.get(contract=obj)
                return event.support_contact == request.user
            return request.user == obj.sales_contact
        elif request.method == "PUT" and obj.is_signed is True:
            raise PermissionDenied("Cannot update a signed contract")
        return request.user == obj.sales_contact and obj.is_signed is False


class EventPermission(BasePermission):
    """
      SALES:    - Create new events
                - Read their own clients events
                - Update their own clients events if not 'Done'
                - Delete their own clients events if not 'Done'

    SUPPORT:    - Read their own clients events
                - Update their own clients events if not 'Done'
    """

    def has_permission(self, request, view):
        if request.user.role == "SUPPORT":
            return request.method in ["GET", "PUT"]
        return request.user.role == "SALES"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return (
                request.user == obj.contract.sales_contact
                or request.user == obj.support_contact
            )
        else:
            done_status = EventStatus.objects.get(description="Done")
            if obj.status == done_status:
                raise PermissionDenied("Cannot update, event is already done")
            if request.user.role == "SUPPORT":
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact
