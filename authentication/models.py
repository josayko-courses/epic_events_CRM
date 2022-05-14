from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.managers import UserManager


class User(AbstractUser):
    SALES = "SALES"
    SUPPORT = "SUPPORT"
    MANAGEMENT = "MANAGEMENT"
    ROLE_CHOICES = (
        (SALES, "Sales"),
        (SUPPORT, "Support"),
        (MANAGEMENT, "Management"),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    username = None
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.role}"

    def save(self, *args, **kwargs):
        """
        Save the user instance
        """
        self.is_staff = True
        user = super(User, self)
        user.save()
        return user
