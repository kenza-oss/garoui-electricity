from django.urls import path
from . import views

app_name = 'devis'

urlpatterns = [
    path('', views.demande_devis, name='demande'),
    path('confirmation/', views.confirmation_devis, name='confirmation'),
]
