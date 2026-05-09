from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('register/', views.partner_register, name='partner_register'),
]
