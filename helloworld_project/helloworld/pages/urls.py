from django.urls import path
from .views import CartRemoveAllView, CartView, ContactPageView, HomePageView, AboutPageView, ProductIndexView, ProductShowView, TemplateView, ProductListView, ProductCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create/', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/list/', ProductListView.as_view(), name='list' ),
    path('products/created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]