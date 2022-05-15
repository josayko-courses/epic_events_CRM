from django.db import models
from config.settings import AUTH_USER_MODEL
from crm.models import Client


class Contract(models.Model):
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_signed = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due = models.DateTimeField()

    sales_contact = models.ForeignKey(
        AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.client}"
