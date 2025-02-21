from django.urls import path
from .views import ProductIndexView, ProductShowView

urlpatterns = [
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<int:id>', ProductShowView.as_view(), name='show'),
]