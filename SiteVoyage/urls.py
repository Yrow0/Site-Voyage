from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_voyage.urls")),

    path("clients/", include("django.contrib.auth.urls")),
    path("clients/", include("clients.urls")),
]
