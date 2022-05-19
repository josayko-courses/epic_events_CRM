from django.db import models

from config.settings import AUTH_USER_MODEL


class Client(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32, blank=True)
    company_name = models.CharField(max_length=64)

    is_customer = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    sales_contact = models.ForeignKey(
        AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.company_name} - {self.email}"
