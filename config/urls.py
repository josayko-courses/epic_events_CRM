from django.contrib import admin
from django.urls import include, path

from authentication import views


def test(request):
    division = 1 / 0
    return division


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", views.login_page, name="login"),
    path("crm/", include("crm.urls")),
    path("test/", test),
]
