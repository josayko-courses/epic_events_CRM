from django.db import models
from config.settings import AUTH_USER_MODEL
from contracts.models import Contract


class EventStatus(models.Model):
    description = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Event Status"
        verbose_name_plural = "Event Status"

    def __str__(self):
        return f"{self.description}"


class Event(models.Model):
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=256, blank=True)

    NOT_OPEN = "NOT_OPEN"
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    STATUS_CHOICES = (
        (NOT_OPEN, "Not Open"),
        (OPEN, "Open"),
        (CLOSE, "Close"),
    )

    status = models.ForeignKey(EventStatus, null=True, on_delete=models.SET_NULL)
    support_contact = models.ForeignKey(
        AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    contract = models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.contract}"
