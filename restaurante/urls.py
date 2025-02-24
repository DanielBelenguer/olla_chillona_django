from django.urls import path
from . import views
from django.urls import include



urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("registro/", views.register_view, name="register_view"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path ("list_platos/" , views.list_platos, name="list_platos"),
    path("add_plato/", views.add_plato, name="add_plato"),
    path("ver_plato/<int:plato_id>/", views.detail, name="detail"),
    path("edita_plato/<int:plato_id>/", views.edita_plato, name="edita_plato"),
    path("add_descuento/", views.add_descuento, name="add_descuento"),
    path("add_reserva/", views.add_reserva, name="add_reserva"),
    path("add_saldo", views.add_saldo, name="add_saldo"),
    path("add_menu/", views.add_menu, name="add_menu"),
    path("list_menus/", views.list_menus, name="list_menus"),
    path("add_servicio/<int:usuario_id>/", views.add_servicio, name="add_servicio"),
    path("pagar_servicio/<int:servicio_id>/", views.pagar_servicio, name="pagar_servicio"),
    path("historial_servicios/", views.historial_servicios, name="historial_servicios"),
]
