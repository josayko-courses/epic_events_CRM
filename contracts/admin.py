from django.contrib import admin

from contracts.models import Contract, ContractStatus


class ContractStatusAdmin(admin.ModelAdmin):
    model = ContractStatus
    ordering = ("description",)
    list_display = (
        "description",
        "id",
    )


admin.site.register(ContractStatus, ContractStatusAdmin, name="Status")


@admin.register(Contract)
class MyClientAdmin(admin.ModelAdmin):
    model = Contract
    ordering = (
        "name",
        "amount",
        "payment_due",
        "status",
        "sales_contact",
        "client",
        "is_signed",
        "date_created",
        "date_updated",
    )
    list_display = (
        "name",
        "amount",
        "payment_due",
        "status",
        "sales_contact",
        "client",
        "is_signed",
        "date_created",
        "date_updated",
        "id",
    )
