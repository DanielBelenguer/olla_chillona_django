from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("registro/", views.register_view, name="register_view"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path ("list_platos/" , views.list_platos, name="list_platos"),
    path("add_plato/", views.add_plato, name="add_plato"),
    path("<int:plato_id>/", views.detail, name="detail"),
    path("edita_plato/<int:plato_id>/", views.edita_plato, name="edita_plato"),
    path("add_descuento/", views.add_descuento, name="add_descuento"),
    path("add_reserva/", views.add_reserva, name="add_reserva"),
    path("add_saldo", views.add_saldo, name="add_saldo"),
    path("add_menu/", views.add_menu, name="add_menu"),
    path("list_menus/", views.list_menus, name="list_menus")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)