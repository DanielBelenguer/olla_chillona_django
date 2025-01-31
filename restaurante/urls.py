from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_platos/", view=index, name="list_platos")
]

""" path("<int:plato_id>/", views.detail, name="detail"),
    path("add_plato/", views.create, name="add_plato") """