from django.contrib import admin

from events.models import Event, EventStatus


class EventStatusAdmin(admin.ModelAdmin):
    model = EventStatus
    ordering = ("description",)
    list_display = (
        "description",
        "id",
    )


admin.site.register(EventStatus, EventStatusAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    ordering = (
        "name",
        "attendees",
        "event_date",
        "status",
        "support_contact",
        "contract",
    )

    list_display = (
        "name",
        "attendees",
        "event_date",
        "status",
        "support_contact",
        "contract",
        "id",
    )
