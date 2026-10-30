
from django.urls import path
from .views import ProductoView

urlpatterns = [
    path('productos/', ProductoView.as_view(), name='productos'),
    path('productos/<int:pk>/', ProductoView.as_view(), name='producto_detalle'),
]
