from django.urls import path
from rest_producto.views import lista_producto

urlpatterns = [
    path('lista_producto', lista_producto, name="lista_producto"),
]