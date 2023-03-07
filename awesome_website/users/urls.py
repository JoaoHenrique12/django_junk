from django.urls import include, re_path, include
from .views import dashboard

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
]
