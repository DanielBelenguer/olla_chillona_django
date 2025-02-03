from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("registro/", views.register_view, name="register_view"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
