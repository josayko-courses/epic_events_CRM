from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class MyClientAdmin(admin.ModelAdmin):
    model = Client
    ordering = (
        "company_name",
        "first_name",
        "last_name",
        "email",
        "phone",
        "mobile",
        "is_customer",
        "date_created",
        "date_updated",
    )
    list_display = (
        "company_name",
        "first_name",
        "last_name",
        "phone",
        "mobile",
        "date_created",
        "date_updated",
        "id",
    )
