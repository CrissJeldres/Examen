from django.urls import path
from rest_promocion.views import lista_promocion

urlpatterns = [
    path('lista_promocion', lista_promocion, name="lista_promocion"),
]