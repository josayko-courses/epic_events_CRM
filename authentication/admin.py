from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin
from authentication.forms import MyUserChangeForm, MyUserCreationForm


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    ordering = ("email", "role", "first_name", "last_name")
    list_display = (
        "email",
        "role",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "id",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    readonly_fields = ("id",)
    fieldsets = (
        (
            None,
            {"fields": ("id", "email", "password", "role", "first_name", "last_name")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")


admin.site.register(User, MyUserAdmin)