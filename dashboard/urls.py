from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('inventory/', views.inventory, name='inventory'),
    path('customers/', views.customers, name='customers'),
    path('settings/', views.settings_view, name='settings'),
]
