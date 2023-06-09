from django.urls import include, re_path, include
from .views import dashboard, register

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^register/", register, name="register"), # type: ignore
]
