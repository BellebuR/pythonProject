from django.urls import path
from .views import home, product_detail
from .views import add_to_cart, cart_view, remove_from_cart, save_order

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('save-order/', save_order, name='save_order'),
]