from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:handle>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('place-order/', views.place_order, name='place_order'),
]
