from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.managers import UserManager


class User(AbstractUser):
    SALES = "SALES"
    SUPPORT = "SUPPORT"

    ROLE_CHOICES = (
        (SALES, "Sales"),
        (SUPPORT, "Support"),
    )

    objects = UserManager()

    email = models.EmailField(unique=True)
    username = None
    role = models.CharField(max_length=32, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
