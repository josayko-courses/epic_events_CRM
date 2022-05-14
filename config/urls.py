from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", views.login_page, name="login"),
    path("crm/", include("crm.urls")),
]
