from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("apps.accounts.urls")),
    path("api/v1/", include("apps.dialogs.api.routes")),
]
